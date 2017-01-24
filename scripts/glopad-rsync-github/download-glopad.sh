#!/bin/bash
REMOTE_USER="jgr25"
REMOTE_MACHINE="sf-lib-dig-005.serverfarm.cornell.edu"
REMOTE_PATH="/arts-lib/sites/www.glopad.org"
LOCAL_PATH="/Users/jgr25/Documents/www-glopad-org"


rsync -avcz -e "ssh -l $REMOTE_USER" \
  --exclude=cache \
  --exclude=templates_c \
  --exclude=var/tmp \
  --exclude=drupal_files \
  --exclude=media \
  --exclude=old_cache \
  --exclude=htdocs/phpPgAdmin \
  --exclude=.svn --exclude=.git --exclude=.gitignore \
  --exclude=.DS_Store \
  --exclude=htdocs/jparc/files \
  $REMOTE_USER@$REMOTE_MACHINE:$REMOTE_PATH/ $LOCAL_PATH/ || error_exit "can't move site files"
