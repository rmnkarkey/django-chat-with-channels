import json
import asyncio
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.consumer import AsyncConsumer
from channels.layers import get_channel_layer


class ChatConsumer(AsyncConsumer):
    
    async def websocket_connect(self,event):

        self.room_name = self.scope['url_route']['kwargs']['room_id']
        self.ids = self.scope['url_route']['kwargs']['users_id']
        self.category_id = self.scope['url_route']['kwargs']['category_name_id']

        self.room_group_name = 'chat_{}{}{}'.format(self.category_id,self.room_name,self.ids)

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.send({
            'type':"websocket.accept",
        })        


    async def websocket_disconnect(self,event):
        pass

    async def websocket_receive(self,event):
        font_text = event.get('text')
        myResponse ={
            'message':font_text
        }
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':json.dumps(myResponse)
            }
        ) 
    
    async def chat_message(self, event):
        await self.send({
            'type':'websocket.send',
            'text':event['message']
        })