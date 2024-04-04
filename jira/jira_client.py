'''
This module handles the Jira API client and provides functions to fetch tasks and their status.
'''
from jira import JIRA
import os

class JiraClient:
    def __init__(self, username, password, url):
        self.username = username
        self.password = password
        self.url = url
        self.jira = JIRA(server=self.url, basic_auth=(self.username, self.password))
    def get_unassigned_todo_tasks(self):
        return self.jira.search_issues('project = "RO" and status = ToDo and assignee = empty ORDER BY created DESC', maxResults=None)
    def get_task_attachments(self, issue):
        attachments = []
        for attachment in issue.fields.attachment:
            print("Name: '{filename}', size: {size}".format(
                filename=attachment.filename, size=attachment.size))
            attachments.append(Attachment(attachment.id,attachment.filename,attachment.get()))
        return attachments
    
    def delete_all_task_attachments(self, issue):
        for attachment in issue.fields.attachment:
            self.jira.delete_attachment(attachment.id)
    def add_task_attachment(self, issue, filepath):
        self.jira.add_attachment(issue=issue, attachment=filepath)
    def add_task_attachments(self, issue, path):
        for entry in os.scandir(path):
            if entry.is_file():
                self.jira.add_attachment(issue=issue, attachment=entry.path)

class Attachment:
    def __init__(self, id, name, data):
        self.id = id
        self.name = name
        self.data = data