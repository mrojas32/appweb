import { Outlet } from "react-router-dom";
import Navbar from "../components/Navbar";

const LayoutAdmin = () => {
    return (
        <>
            <Navbar />
            <main className="container text-center">
                <Outlet />
            </main>
        </>
    );
};
export default LayoutAdmin;
