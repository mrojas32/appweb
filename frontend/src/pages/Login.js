import { Button, Dialog, DialogActions, DialogContent, DialogTitle, TextField } from "@mui/material";
import { useState } from "react"

export default function Login() {
    
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
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
                type='password'
                label='Contraseña'
                value={password}
                onChange={e => setPassword(e.target.value)}
            />
            <Button variant='outlined' color='primary' onClick={() => setDialogOpen(true)}>
                Entrar
            </Button>

            <Dialog open={dialogOpen} onClose={() => setDialogOpen(false)}>
                <DialogTitle> Titulo </DialogTitle>
                <DialogContent> Dialog content here... </DialogContent>
                <DialogActions>
                    <Button onClick={() => setDialogOpen(false)}>
                        Close
                    </Button>
                </DialogActions>
            </Dialog>
        </div>
    )
}
