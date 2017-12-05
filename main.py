#!/usr/bin/env python
import cgitb
import random
import YourFormProcessor

cgitb.enable() # Will catch tracebacks and errors for you. Comment it out if you no-longer need it.

if __name__ == '__main__':
  YourFormProcessor.Process_Form() # This is your logic to process the form.

  redirectURL = "willper.me"

  print 'Content-Type: text/html'
  print 'Location: %s' % redirectURL
  print # HTTP says you have to have a blank line between headers and content
  print '<html>'
  print '  <head>'
  print '    <meta http-equiv="refresh" content="0;url=%s" />' % redirectURL
  print '    <title>You are going to be redirected</title>'
  print '  </head>' 
  print '  <body>'
  print '    Redirecting... <a href="%s">Click here if you are not redirected</a>' % redirectURL
  print '  </body>'
  print '</html>'