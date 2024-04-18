import { Router, createBrowserRouter } from "react-router-dom";

import LayoutAdmin from "../Layout/LayoutAdmin";
import HomeAdmin from "../pages/HomeAdmin";
import Gestion from "../pages/Gestion";
import Reportes from "../pages/Reportes";


export const router = createBrowserRouter([
    {
        path: "/",
        element: <LayoutAdmin />,
        children: [
            {
                index: true,
                element: <HomeAdmin />,
            },
            {
                path: "/gestion",
                element: <Gestion />,
            },
            {
                path: "/reportes",
                element: <Reportes />,      
            }
        ]
    },

]);