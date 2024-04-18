import { Router, createBrowserRouter } from "react-router-dom";

import LayoutAdmin from "../Layout/LayoutAdmin";
import HomeLogin from "../pages/HomeLogin";
import Reservar from "../pages/Reservar";



export const router = createBrowserRouter([
    {
        path: "/",
        element: <LayoutAdmin />,
        children: [
            {
                index: true,
                element: <HomeLogin />,
            },
            {
                path: "/reservar",
                element: <Reservar />,
            }
        ]
    },

]);