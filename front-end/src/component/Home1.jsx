import { useNavigate } from 'react-router-dom';
const Home1 = () => {
  const navigate=useNavigate()

    return (
      <div className="h-screen w-full justify-center items-center flex flex-col gap-4">
        <form className=" bg-gray-300 flex flex-col w-2/5 justify-center items-center rounded-xl h-[70vh] gap-5">
        <p className="poppins text-3xl ">welcome</p>
    <p className="poppins text-xl"> pour voir l'emplois du temps de les etudient cliquez sur :</p>
     <button onClick={()=>{navigate('/std')}} className="w-36 bg-red-600 text-white h-8 rounded-lg">clicker</button>
    <p className="poppins text-xl "> pour voir l'emplois du temps de les enseignants cliquez sur :</p>
   
     <button onClick={()=>{navigate('/t')}} className="w-36 bg-red-600 text-white h-8 rounded-lg">clicker</button>
     <p className="poppins text-xl "> pour ajouter un creneau pour un enseignants:</p>
   
   <button onClick={()=>{navigate('/k')}} className="w-36 bg-red-600 text-white h-8 rounded-lg">clicker</button>
</form>
      </div>
    );
  }
  
  export default Home1;
  