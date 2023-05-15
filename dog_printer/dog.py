import os
from subprocess import run
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


sync_target = os.path.join(os.getenv('HOME'), 'Descargas')
company_name = 'fuxia_men'


class DogEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        """Detect modifications in sync_target folder
        to figure out if there is a dolibarr pdf file
        that must be printed
        """
        # dolibarr files from ticket are saved by default
        # as recipe.php.pdf, so, we are only detect that
        # kind of file
        if event.scr_path.endswith('.php.pdf'):
            # rename document to avoid name collision later
            # and have files correctly labeled
            new_filename = os.path.join(sync_target, datetime.now().strftime(f'factura_{company_name}_%Y_%m_%d__%H_%M_%S.pdf'))
            os.rename(event.src_path, new_filename)
            # print document on cups thermal printer
            self.print_doc(new_filename)

    def print_doc(self, filename:str):
        """Print a given document in cups printer
        if you want to see your installed cups printer
        paste this in your shell:

        lpstat -p -d

        https://www.cups.org/doc/options.html
        """
        # i installed xprinter XP-58 as xp58
        cups_printer_name = 'xp58'
        # print order can be found in the link below
        print_order = ['lp', '-d', cups_printer_name, filename]
        run(print_order, check=True)


if __name__ == '__main__':
    observer = Observer()
    observer.schedule(DogEventHandler(), sync_target, recursive=False)
    observer.start()
    try:
        while observer.is_alive():
            observer.join(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()