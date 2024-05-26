import { Button, Input, Step, StepLabel, Stepper } from "@mui/material";
import { useEffect, useState } from "react";

const DUMMY_HORAS = [
    { hora: '8:00', disponible: true },
    { hora: '9:00', disponible: true },
    { hora: '10:00', disponible: true },
    { hora: '11:00', disponible: false },
    { hora: '12:00', disponible: true },
    { hora: '13:00', disponible: true },
    { hora: '14:00', disponible: false },
    { hora: '15:00', disponible: false },
    { hora: '16:00', disponible: false },
    { hora: '17:00', disponible: true },
    { hora: '18:00', disponible: true },
];


export default function Reserva(){
    const STEPS = ['calendario', 'reserva', 'confirmar'];
    const [stepIndex, setStepIndex] = useState(0);
    const [fecha, setFecha] = useState(null);
    const [hora, setHora] = useState(null);
    const [horas, setHoras] = useState(null);

    const handleSelectHora = (newHora) => {
        setHora(newHora);
        setStepIndex(2);
    };

    useEffect( () => {
        setHoras(DUMMY_HORAS);
    }, []);

    useEffect( () => {
        if (stepIndex === 0) setHora(null);
    }, [stepIndex])
    
    return (
        <div className='flex flex-col mt-[10vh] gap-8 justify-center'>
            <Stepper activeStep={STEPS[stepIndex]}>
                <Step
                    key={STEPS[0]}
                    active={stepIndex === 0}
                    completed={stepIndex > 0}
                >
                    <StepLabel> Calendario </StepLabel>
                </Step>
                <Step
                    key={STEPS[1]}
                    active={stepIndex === 1}
                    completed={stepIndex > 1}
                >
                    <StepLabel> Seleccion de Hora </StepLabel>
                </Step>
            </Stepper>
            <div className='flex flex-col gap-3 md:w-[50vw] max-w-lg'>
                <div className='flex flex-col gap-1'>
                { fecha && <div className='text-lg text-right'> Fecha Seleccionada: {fecha} </div> }
                { hora && <div className='text-lg text-right'> Hora Seleccionada: {hora} </div> }
                </div>

                { stepIndex === 0 && (
                        <>
                            <input 
                                type='date'
                                className='text-black p-2 rounded-md bg-slate-300'
                                value={fecha}
                                onChange={(e) => setFecha(e.target.value)}
                            />
                            <Button
                                variant='contained'
                                color='primary'
                                onClick={() => setStepIndex(1)}
                                disabled={!fecha}
                            >
                                Confirmar Fecha
                            </Button>
                        </>
                    )
                }
                { stepIndex === 1 && (
                        <>
                            <Button
                                variant='contained'
                                color='warning'
                                size='small'
                                onClick={() => setStepIndex(0)}
                            >
                                Volver
                            </Button>
                            <div className='grid grid-cols-3 gap-1'>
                            {horas.map(hora => (
                                <Button
                                    variant='outlined'
                                    color='secondary'
                                    disabled={!hora.disponible}
                                    onClick={() => handleSelectHora(hora.hora)}
                                >
                                    {hora.hora}
                                </Button>
                            ))}
                            </div>
                        </>
                    )
                }
                { stepIndex === 2 && (
                        <div className='grid grid-cols-2 mt-3 gap-2'>
                            <Button
                                variant='contained'
                                color='warning'
                                onClick={() => setStepIndex(0)}
                            >
                                Volver
                            </Button>
                            <Button
                                variant='contained'
                                color='success'
                                onClick={() => alert('agendar hora')}
                            >
                                Confirmar
                            </Button>
                        </div>
                    )
                }
            </div>
        </div>
    );
}
