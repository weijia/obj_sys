import socket
import logging
from libtool import format_path


def get_fs_protocol_separator():
    try:
        import configurationTools as config
        return config.getFsProtocolSeparator()
    except ImportError:
        return "://"


gUfsObjUrlPrefix = u'ufs' + get_fs_protocol_separator()
gUfsObjUrlSeparator = u'/'

log = logging.getLogger(__name__)


def is_web_url(url):
    # log.error(url)
    if is_ufs_url(url):
        protocol, content = parse_url(url)
        if protocol in ["https", "http", "ftp"]:
            return True
    return False


def get_formatted_full_path(full_path):
    return format_path(full_path)


def parse_url(url):
    return url.split(get_fs_protocol_separator(), 2)


def get_hostname():
    return unicode(socket.gethostname())


def get_ufs_url_for_local_path(full_path):
    return gUfsObjUrlPrefix + get_hostname() + gUfsObjUrlSeparator + format_path(full_path)


def get_full_path_from_ufs_url(ufs_url):
    if not is_ufs_fs(ufs_url):
        raise "not ufs url"
    objPath = parse_url(ufs_url)[1]
    hostname, full_path = objPath.split(gUfsObjUrlSeparator, 1)
    # print hostname, full_path
    if unicode(hostname) != get_hostname():
        raise 'not a local file'
    return full_path


def get_full_path_for_local_os(ufs_url):
    url_content = parse_url(ufs_url)[1]
    if '/' == url_content[0]:
        # The path returned by qt is file:///d:/xxxx, so we must remove the '/' char first
        return url_content[1:]
    return url_content


def is_uuid(url):
    return url.find(u"uuid" + get_fs_protocol_separator()) == 0


def get_url_content(url):
    protocol, content = parse_url(url)
    return content


def get_path_for_ufs_url(url):
    url_content = get_url_content(url)
    return url_content.split(gUfsObjUrlSeparator, 1)[1]


def get_uuid(url):
    return get_url_content(url)


def get_url_for_uuid(id):
    return u"uuid" + get_fs_protocol_separator() + id


def is_ufs_url(url):
    """
    In format of xxxx://xxxx
    :param url:
    """
    if url.find(get_fs_protocol_separator()) == -1:
        return False
    else:
        return True


def get_ufs_local_root_url():
    return gUfsObjUrlPrefix + get_hostname() + gUfsObjUrlSeparator


def is_ufs_fs(url):
    return url.find(gUfsObjUrlPrefix) == 0


def get_ufs_basename(url):
    return url.rsplit(gUfsObjUrlSeparator, 1)[1]


def get_host(ufs_url):
    if is_ufs_fs(ufs_url):
        path_with_host = parse_url(ufs_url)[1]
        return path_with_host.split(u"/")[0]
    raise "Not Ufs URL"


def is_local(ufs_url):
    """
    ufs_url in format ufs://hostname/D:/tmp/xxx.xxx
    """
    if get_host(ufs_url) == get_hostname():
        return True
    else:
        print "not local", get_host(ufs_url), get_hostname()
        return False
