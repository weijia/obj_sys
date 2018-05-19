import os
from optparse import make_option

from django.core.management import BaseCommand

from djangoautoconf.cmd_handler_base.msg_process_cmd_base import DjangoCmdBase
from obj_sys.models_ufs_obj import UfsObj


class FileTagger(DjangoCmdBase):
    option_list = BaseCommand.option_list + (
        make_option('--tags',
                    action='store',
                    dest='tags',
                    type='string',
                    help='Tags separated with ","'),
        make_option('--file_path',
                    action='store',
                    dest='file_path',
                    type='string',
                    help='Path of the file to be tagged'),
        make_option('--log-file',
                    action='store',
                    dest='log_file',
                    help='Log file destination'),
        make_option('--log-std',
                    action='store_true',
                    dest='log_std',
                    help='Redirect stdout and stderr to the logging system'),
    )

    def msg_loop(self):
        # enum_method = enum_git_repo
        # pull_all_in_enumerable(enum_method)
        if os.path.exists(self.options["file_path"]):
            new_file_ufs_obj, is_created = UfsObj.objects.get_or_create(full_path=self.options["file_path"])
            new_file_ufs_obj.tags = self.options["tags"]


Command = FileTagger
