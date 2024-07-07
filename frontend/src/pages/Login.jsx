import { Button, Dialog, DialogActions, DialogContent, DialogTitle, TextField } from "@mui/material";
import { useState } from "react";
import { apiWrapper } from '../libs/fetchWrappers/apiFetch';
import { setToken } from '../dataModel/Session';

export default function Login() {
    
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');


    const handleLogin = () => {
        const params = new URLSearchParams();
        params.append('username', username);
        params.append('password', password);
        apiWrapper.post('/auth', params
            ).then(resp => {
                setToken(resp.access_token);
            }).catch( err => console.log(err) );
    }

    return (
        <div className='flex flex-col gap-3 max-w-md bg-slate-900 rounded p-5 mt-20'>
            <TextField
                type='text'
                label='Usuario'
                value={username}
                onChange={e => setUsername(e.target.value)}
            />
            <TextField
                type='password'
                label='Contraseña'
                value={password}
                onChange={e => setPassword(e.target.value)}
            />
            <Button variant='outlined' color='primary' onClick={handleLogin}>
                Entrar
            </Button>
        </div>
    )
}
