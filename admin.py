from djangodblog.models import Error, ErrorBatch
from djangodblog.admin import ErrorBatchAdmin, ErrorAdmin

admin.site.unregister(Error)
admin.site.unregister(ErrorBatch)
admin.site.register(Error, ErrorAdmin)
admin.site.register(ErrorBatch, ErrorBatchAdmin)
