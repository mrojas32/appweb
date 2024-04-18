import { Button, Dialog, DialogActions, DialogContent, DialogTitle, TextField } from "@mui/material";
import { useState } from "react"
import { Route, Routes } from 'react-router-dom';
import { Navbar } from '../Navbar';

export default function Usuario() {
  const [userName, setUserName] = useState('Juanito'); // Nombre de usuario inicial
  const [dialogOpen, setDialogOpen] = useState('');

  return (
    <>
    <Routes>
        <Route path='/' element={<Navbar />}></Route>
    </Routes>
      <div>
        <Button variant='outlined' color='primary' onClick={() => setDialogOpen(true)}>
                Eliminar Usuario
        </Button>

        <Dialog open={dialogOpen} onClose={() => setDialogOpen(false)}>
            <DialogTitle> Titulo </DialogTitle>
            <DialogContent> Usuario eliminado </DialogContent>
            <DialogActions>
                <Button onClick={() => setDialogOpen(false)}>
                    Close
                </Button>
            </DialogActions>
        </Dialog>
      </div>
    </>
  )
}


