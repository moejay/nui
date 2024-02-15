
import { writable } from "svelte/store";
import * as api from "../client/index";

export const stateTree = writable({} as api.StateTree);

let socket = null;

export const connect = () => {
    console.log('connecting to server');
    socket = new WebSocket('ws://localhost:8000/ws');
    socket.onopen = () => {
        console.log('connected to server');
    };

    socket.onmessage = (event) => {
        const data = JSON.parse(event.data);
        stateTree.set(data);
    };

    socket.onclose = () => {
        console.log('disconnected from server');
    };
};

export const sendMessage = (message: string) => {
    socket.send(JSON.stringify({
        "message": message,
    }));
}

export const messageHistory = writable([] as string[]);