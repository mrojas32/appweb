import { Button, Dialog, DialogActions, DialogContent, DialogTitle, TextField } from "@mui/material";
import { useState } from "react"

export default function Registro() {
    
    const [username, setUsername] = useState('');
    const [correo, setCorreo] = useState('');
    const [password, setPassword] = useState('');
    const [r_password, setR_Password] = useState('');
    const [dialogOpen, setDialogOpen] = useState('');

    return (
        <div className='flex flex-col gap-3 max-w-md bg-slate-900 rounded p-5 mt-20'>
            <TextField
                type='text'
                label='Usuario'
                value={username}
                onChange={e => setUsername(e.target.value)}
            />
            <TextField
                type='text'
                label='Correo'
                value={correo}
                onChange={e => setCorreo(e.target.value)}
            />
            <TextField
                type='password'
                label='Contraseña'
                value={password}
                onChange={e => setPassword(e.target.value)}
            />
           <TextField
                type='password'
                label='Confirmar Contraseña'
                value={r_password}
                onChange={e => setR_Password(e.target.value)}
            />
            <Button variant='outlined' color='primary' onClick={() => setDialogOpen(true)}>
                Entrar
            </Button>

            <Dialog open={dialogOpen} onClose={() => setDialogOpen(false)}>
                <DialogTitle> Titulo </DialogTitle>
                <DialogContent> Usario ingresado</DialogContent>
                <DialogActions>
                    <Button onClick={() => setDialogOpen(false)}>
                        Close
                    </Button>
                </DialogActions>
            </Dialog>
        </div>
    )
}
