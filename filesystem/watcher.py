"""
Ability to watch the given file system and act for create/modify/delete
"""
from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer


class FileWatcher(PatternMatchingEventHandler):
    """
    An implementation for file watcher, default to observe all files
    """

    def __init__(self, patterns="*", ignore_patterns="",
                 ignore_directories=True, case_sensitive=False):
        super(FileWatcher, self).__init__(patterns=patterns, ignore_patterns=ignore_patterns,
                                          ignore_directories=ignore_directories, case_sensitive=case_sensitive)


def create_observer(root_dir, created_cb, deleted_cb, modified_cb, moved_cb):
    """
    Creates an observer for the given root directory
    example:
            fs_thread = threading.Thread(target=lambda: observer.start())
            fs_thread.setDaemon(True)
            observer = create_fs_observer(report.app_temp_directory)
            fs_thread.start()
            fs_thread.join()

    :param root_dir: the directory to watch
    :param created_cb: a callback for created files
    :param deleted_cb:  a callback for deleted files
    :param modified_cb: a callback for modified files
    :param moved_cb: a callback for moved files
    :return:
    """
    # Creating the observer
    observer = Observer()
    watcher = FileWatcher()

    # Register on events
    watcher.on_created = created_cb
    watcher.on_deleted = deleted_cb
    watcher.on_modified = modified_cb
    watcher.on_moved = moved_cb

    # schedule the observer (not starting it)
    observer.schedule(watcher, root_dir)
    # return the observer obj so initiator can start and control it
    return observer
