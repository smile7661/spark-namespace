from django.contrib import admin
from WeeklyReport.models import report


class reportAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(reportAdmin, self).get_queryset(request)
        print(qs)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(report_name=request.user)

    list_display = ('report_name', 'report_date', 'report_redflag', 'report_achievements', 'report_supportNeeded')


class UsersAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_password', 'user_email')


# Register your models here.
admin.site.register(report, reportAdmin)
