class ObjSysClint(object):
    def __init__(self):
        super(ObjSysClint, self).__init__()
        self.password = "richard"
        self.username = "richard"
        self.server_port = 8110
        self.server_name = "127.0.0.1"

    def get_server_and_port_str(self):
        if not (self.server_port is None):
            return "%s:%s" % (self.server_name, self.server_port)
        else:
            return "%s" % self.server_name

    def get_manual_tagging_url_for_qt_urls(self, urls_str):
        """
        Get URL for manually tagging object identified with URL
        :param urls_str: urls connected with "&". For example: "http://google.com&http://g.cn"
        :return: N/A
        """
        return "http://%s/webmanager/login_and_go_home/?" \
               "username=%s&password=%s&target=" \
               "/obj_sys/tagging_local/?%s" % (
                   self.get_server_and_port_str(), self.username, self.password, urls_str
               )

    def get_post_tag_url(self, url, tags):
        return "https://%s/obj_sys/append_tags/?username=%s&password=%s" \
               "&selected_url=%s&description=&tags=star" % (
            self.get_server_and_port_str(), self.username, self.password, url, tags)
