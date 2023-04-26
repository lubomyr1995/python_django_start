import {useEffect, useState} from 'react'
import {autoParkService, socketService} from '../../services'
import {AutoPark} from '../AutoPark/AutoPark'
import {AutoParkForm} from '../AutoParkForm/AutoParkForm'
import {Chat} from '../Chat/Chat'
import css from './AutoParks.module.css'


const AutoParks = () => {
    const [autoParks, setAutoParks] = useState([])
    const [chatSocket, setChatSocket] = useState(null)
    const [messages, setMessages] = useState([])

    useEffect(() => {
        autoParkSocketInit().then()
    }, [])

    useEffect(() => {
        autoParkService.getAll().then(value => value.data).then(value => setAutoParks(value))
    }, [])

    useEffect(() => {
        chatSocketInit().then(value => setChatSocket(value))
    }, [])

    const chatSocketInit = async () => {
        const client = await socketService.chat()
        // console.log(client);

        client.onopen = () => {
            console.log('Chat socket connected')
        }
        client.onmessage = (msg) => {
            // const data = JSON.parse(msg.data)
            const data = JSON.parse(`${msg.data}`)
            // console.log(msg.data)
            setMessages(prev => [...prev, data])
        }
        return client
    }

    const autoParkSocketInit = async () => {
        const client = await socketService.autoParks()
        client.onopen = () => {
            console.log('AutoPark socket connected')
            client.send(JSON.stringify({
                action: 'subscribe_to_auto_park_activity',
                request_id: new Date().getTime()
            }))
        }
        client.onmessage = (msg) => {
            const data = JSON.parse(`${msg.data}`)
            // console.log(data);
            setAutoParks(prevState => [...prevState, data.data])
        }
        return client
    }

    return (
        <div className={css.AutoPark}>
            <div>
                <AutoParkForm setAutoParks={setAutoParks}/>
                <hr/>
                <div>
                    {autoParks.map(autoPark => <AutoPark key={autoPark.id} autoPark={autoPark}/>)}
                </div>
            </div>
            <Chat chatSocket={chatSocket} messages={messages}/>
        </div>
    )
}

export {AutoParks}