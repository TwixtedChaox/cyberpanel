from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.loadEmailHome, name='loadEmailHome'),
    re_path(r'^createEmailAccount$', views.createEmailAccount, name='createEmailAccount'),
    re_path(r'^listEmails$', views.listEmails, name='listEmails'),
    re_path(r'^submitEmailCreation$', views.submitEmailCreation, name='submitEmailCreation'),
    re_path(r'^fetchEmails$', views.fetchEmails, name='fetchEmails'),

    ## Mail Forwardings
    re_path(r'^emailForwarding$', views.emailForwarding, name='emailForwarding'),
    re_path(r'^submitEmailForwardingCreation$', views.submitEmailForwardingCreation, name='submitEmailForwardingCreation'),
    re_path(r'^fetchCurrentForwardings$', views.fetchCurrentForwardings, name='fetchCurrentForwardings'),
    re_path(r'^submitForwardDeletion$', views.submitForwardDeletion, name='submitForwardDeletion'),

    ## Email Aliases
    re_path(r'^emailAliases$', views.emailAliases, name='emailAliases'),
    re_path(r'^fetchEmailAliases$', views.fetchEmailAliases, name='fetchEmailAliases'),
    re_path(r'^submitEmailAliasCreation$', views.submitEmailAliasCreation, name='submitEmailAliasCreation'),
    re_path(r'^submitEmailAliasDeletion$', views.submitEmailAliasDeletion, name='submitEmailAliasDeletion'),

    ## Delete email
    re_path(r'^deleteEmailAccount$', views.deleteEmailAccount, name='deleteEmailAccount'),
    re_path(r'^getEmailsForDomain$', views.getEmailsForDomain, name='getEmailsForDomain'),
    re_path(r'^submitEmailDeletion$', views.submitEmailDeletion, name='submitEmailDeletion'),
    re_path(r'^fixMailSSL$', views.fixMailSSL, name='fixMailSSL'),

    ## Change email password
    re_path(r'^changeEmailAccountPassword$', views.changeEmailAccountPassword, name='changeEmailAccountPassword'),
    re_path(r'^submitPasswordChange$', views.submitPasswordChange, name='submitPasswordChange'),

    ## DKIM Manager
    re_path(r'^dkimManager$', views.dkimManager, name='dkimManager'),
    re_path(r'^fetchDKIMKeys$', views.fetchDKIMKeys, name='fetchDKIMKeys'),
    re_path(r'^generateDKIMKeys$', views.generateDKIMKeys, name='generateDKIMKeys'),

    re_path(r'^installOpenDKIM$', views.installOpenDKIM, name='installOpenDKIM'),
    re_path(r'^installStatusOpenDKIM$', views.installStatusOpenDKIM, name='installStatusOpenDKIM'),

    ### email limits
    re_path(r'^EmailLimits$', views.EmailLimits, name='EmailLimits'),
    re_path(r'^SaveEmailLimitsNew$', views.SaveEmailLimitsNew, name='SaveEmailLimitsNew'),
]
