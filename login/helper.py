scopes = ['https://www.googleapis.com/auth/calendar']    
import datetime
import os
from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from pickle import dump, load

def authorize(id):
    flow = InstalledAppFlow.from_client_secrets_file(f'credentials.json', scopes=scopes)
    if os.path.exists(f'cred-{id}.pkl'):
        return 1
    else:
        try:
            cred = flow.run_local_server(port=5000)

        except Exception:
            return -1
        
        dump(cred, open(f"cred-{id}.pkl", "wb"))
        return 0

def create_appointment(title, start_time, end_time, description, id):
    
    flow = InstalledAppFlow.from_client_secrets_file(f'credentials.json', scopes=scopes)
    
    event = {
              'summary': title,
              'description': description,
              'start': {
                    'dateTime': start_time,
                    'timeZone': 'UTC',
                        },
              'end': {
                    'dateTime': end_time,
                    'timeZone': 'UTC',}}

    if os.path.exists(f'cred-{id}.pkl'):
        cred = load(open(f"cred-{id}.pkl", "rb"))
        service = build('calendar', 'v3', credentials=cred)
        event = service.events().insert(calendarId='primary', body=event).execute()
        return print('Event created: %s' % (event.get('htmlLink')))
    
    else:
        return -1
    