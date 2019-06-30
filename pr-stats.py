import requests
import datetime
import calendar
import argparse


version = "1.0"
user = "subzik"
parser = argparse.ArgumentParser()

parser.add_argument("-u", "--user", help="user", action="store_true")
parser.add_argument("--repo", required=True, help="insert number of github pull-request")
parser.add_argument("-v", "--version", help="version script", version="ver. 1.0", action="version")
parser.add_argument("-o", "--open", help="Info about time open pull", action="store_true")
parser.add_argument("-d", "--dayofweek", help="Day of the week opened", action="store_true")
parser.add_argument("-ho", "--hours", help="Hours of the day opened", action="store_true")
parser.add_argument('-wo', "--weeks", help='Weeks opened', action="store_true")
parser.add_argument("-lu", "--last_user", help="user", action="store_true")
parser.add_argument("--token", type=str, default="dd286dd8f2d0ed9d46fb98c943c7a00456d72037")


args = parser.parse_args()

if args.repo:
    pull_num = args.repo
else:
    pull_num = 17


url = 'https://api.github.com/repos/alenaPy/devops_lab/pulls/%s' % pull_num
pulls = requests.get(url, auth=(user, args.token))
pullsjson = pulls.json()
jsondate = pullsjson['created_at']
converted_created_at = datetime.datetime.strptime(jsondate, "%Y-%m-%dT%H:%M:%SZ")
d_opened = datetime.datetime.now() - converted_created_at
d_of_week = calendar.day_name[converted_created_at.weekday()]
h_ofday = converted_created_at.hour
week = converted_created_at.strftime('%U')
u_opened = pullsjson['user']['login']


if args.open:

    print("Counts opened: ", str(d_opened.days))
if args.dayofweek:
    print("Day of the week opened: ", d_of_week)
if args.hours:
    print("Hours of the day opened: ", str(h_ofday))
if args.weeks:
    print('Week_opened_PR: ',  week)
if args.last_user:
    if args.repo is not None:
        print("User, who opened repo number", args.repo, "is:", u_opened)
    else:
        pull_num = input('Please type repo\'s number: ')

