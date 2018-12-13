import os
import grp
from pathlib import Path

def up(config, conn, semester, course):

    course_dir = Path(config.submitty['submitty_data_dir'], 'courses', semester, course)
    results_public_dir = Path(course_dir, 'results_public')

    # create the directories
    os.makedirs(str(results_public_dir), exist_ok=True)

    php_user = config.submitty_users['php_user']

    # get course group
    stat_info = os.stat(str(course_dir))
    course_group_id = stat_info.st_gid
    course_group = grp.getgrgid(course_group_id)[0]

    # set the owner/group/permissions
    os.system("chown -R "+php_user+":"+course_group+" "+str(results_public_dir))
    os.system("chmod -R u+rwx "+str(results_public_dir))
    os.system("chmod -R g+rxs "+str(results_public_dir))
    os.system("chmod -R o-rwx "+str(results_public_dir))

    
def down(config, conn, semester, course):
    pass
