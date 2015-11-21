class ObjSysClint(object):
    def __init__(self):
        super(ObjSysClint, self).__init__()
        self.password = "richard"
        self.username = "richard"
        self.server_port = 8110
        self.server_name = "127.0.0.1"

    def get_manual_tagging_url(self, urls_str):
        """
        Get URL for manually tagging object identified with URL
        :param urls_str: urls connected with "&". For example: "http://google.com&http://g.cn"
        :return: N/A
        """
        return "http://%s:%s/webmanager/login_and_go_home/?" \
               "username=%s&password=%s&target=" \
               "/obj_sys/tagging_local/?%s" % (
                   self.server_name, self.server_port, self.username, self.password, urls_str
               )
