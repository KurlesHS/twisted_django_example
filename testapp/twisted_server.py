import os
import sys
import threading
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor
from twisted.web import static, wsgi, server, resource
from twisted.python import log
import testapp.wsgi as wsgi_local


# Environment setup for your Django project files:
class Root(resource.Resource):
    def __init__(self, wsgi_resource):
        resource.Resource.__init__(self)
        self.wsgi_resource = wsgi_resource

    def getChild(self, path, request):
        path0 = request.prepath.pop(0)
        request.postpath.insert(0, path0)
        return self.wsgi_resource


class FileNoDir(static.File):
    def directoryListing(self):
        return resource.ForbiddenResource()


sys.path.append("testapp")
os.environ['DJANGO_SETTINGS_MODULE'] = 'testapp.settings'
log.startLogging(sys.stdout)

media_src = FileNoDir(os.path.join(os.path.abspath("."), "media"))
static_src = FileNoDir(os.path.join(os.path.abspath("."), "static"))

print static_src
res = wsgi.WSGIResource(reactor, reactor.getThreadPool(), wsgi_local.application)
root = Root(res)
root.putChild("media", media_src)
root.putChild("static", static_src)
factory = server.Site(root)

TCP4ServerEndpoint(reactor, 8888).listen(factory)
tid = threading.current_thread().ident
log.msg("main tid " + str(tid))
reactor.run()