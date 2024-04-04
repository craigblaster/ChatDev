'''
This is the main entry point of the CLI app.
'''
import argparse
from jira_client import JiraClient
def parse_arguments():
    parser = argparse.ArgumentParser(description='Jira CLI App')
    parser.add_argument('--username', help='Jira username')
    parser.add_argument('--password', help='Jira password')
    parser.add_argument('--url', help='Jira instance URL')
    return parser.parse_args()
def main():
    args = parse_arguments()
    jira_client = JiraClient(args.username, args.password, args.url)
    tasks = jira_client.get_unassigned_todo_tasks()
    for task in tasks:
        print(f'Task: {task.key}, Status: {task.fields.status.name}')
        jira_client.get_task_attachments(task)
        #jira_client.delete_all_task_attachments(task)
        #jira_client.add_task_attachment(task, 'wiki.md')
        #jira_client.add_task_attachments(task, 'jira/')
if __name__ == '__main__':
    main()