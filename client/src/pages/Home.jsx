import Navbar from '../components/Navbar'
import Hero from "../components/Hero"
import Message from "../components/Message";
import Footer from "../components/Footer";


function  Home (){
    return(
        <div>
            <Navbar/>
            <Hero/>
            <Message/>
            <Footer/>
        </div>
    )
}
export default Home;