import {authService} from './auth.service'
import {w3cwebsocket as W3cWebsocket} from 'websocket'

const baseURl = 'ws://localhost/api/v1'

const connect = async (room) => {
    const {data: {token}} = await authService.getSocketToken()
    return new W3cWebsocket(`${baseURl}/auto_parks/${room}?token=${token}`)
}

const socketService = {
    chat: async () => await connect('chat'),
    autoParks: async () => await connect('auto_park'),
}

export {
    socketService
}