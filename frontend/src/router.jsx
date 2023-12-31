import { createBrowserRouter } from "react-router-dom";
import App from "./App";
import HomePage from "./pages/HomePage";
import NotFound from "./pages/NotFoundPage";
import MyProfilePage from "./pages/MyProfilePage";
import RegisterPage from "./pages/RegisterPage";
import UnderwayPage from "./pages/UnderwayPage";
import EditUnderwayPage from "./pages/EditUnderwayPage";
import ViewUnderwayPage from "./pages/ViewUnderwayPage";

const router = createBrowserRouter([
    {
      path: "/",
      element: <App />,
      children: [
        {
          index: true,
          element: <RegisterPage />,
        },
        {
          path: "/home",
          element: <HomePage />,
        },
        {
          path: "/myprofile",
          element: <MyProfilePage />,
        },
        {
          path: "/underway",
          element: <UnderwayPage />
        },
        {
          path:"/editunderway/:underway_id",
          element:<EditUnderwayPage />
        },
        {
          path: "/viewunderway/:underway_id",
          element: <ViewUnderwayPage />
        }
      ],
      errorElement: <NotFound />,
    },
  ]);
  
  export default router;