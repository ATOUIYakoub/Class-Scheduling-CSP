import { useState } from 'react'
import Tableau from './component/Tableau'
import Tableaustd from './component/Tableaustd'
import G from './component/Fpargrp'
import T from './component/Fparprf'
import M from './component/Fparmod'

import {createBrowserRouter,
  Route,
  Link,
  RouterProvider
} from 'react-router-dom'
import './App.css'
import Home from './component/home'
import Home1 from './component/Home1'

function App() {
const router = createBrowserRouter([
{
  
  path:"/",
  element:<Home1/>
},
{
  
  path:"/k",
  element:<Home/>
},
{
  path:"/std",
  element:<Tableaustd/>
},
{
  path:"/g",
  element:<G/>
},
{
  path:"/m",
  element:<M/>
},
{
  path:"/t",
  element:<T/>
},
{
  path:"/mm",
  element:<Tableau/>
}
]);
  return (
    <>
   
    <RouterProvider router={router} />
    </>
  )
}

export default App
