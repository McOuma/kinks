import React from "react";
import  menpic from "../assets/images/bantu.jpg"
import Message  from "./Message";
import  "./hero.css"


function Hero() {
    return (
        <main>
            <section className="hero">
                <div className="my-hero container pt-4">
                    <div className="row">
                        <div className="col-md-6">
                            <img className="w-100vh" src={menpic} alt="lady"/>
                        </div>
                        <div className="col-md-6">
                            <p className="fs-2 fw-light text-center text-danger">Welcome to Kinks and Queens - Celebrating the Beauty of Afro Kinky Hair!</p>
                            <p>At Kinks and Queens, we embrace the natural beauty and versatility of Afro kinky hair. Our blog is dedicated to empowering Africans and celebrating the unique textures, styles, and stories that make our hair truly magnificent.
                                Join us on a journey of self-discovery, inspiration, and hair care tips tailored specifically for our beautiful community. Whether you're a queen embracing your natural kinks or a king supporting and appreciating the beauty of Afro kinky hair, this is the place for you.</p>
                            <p>Discover the latest trends in Afro-centric hairstyles, learn about the best products to nourish and style your hair, and find inspiration from our community of confident individuals who proudly rock their crowns of glorious coils, curls, and kinks.
                                Kinks and Queens is more than just a blog – it's a celebration of heritage, culture, and self-love. Let us guide you through the world of Afro kinky hair, where every strand tells a story, and every curl is a symbol of strength and resilience.</p>
                            <p>Join our passionate community and become part of a movement that embraces and celebrates the natural beauty of Afro kinky hair. Together, we will redefine standards of beauty and empower each other to embrace our authentic selves.
                                Celebrate your kinks, embrace your curls, and reign as a true queen or king with Kinks and Queens. Let your hair journey begin here!</p>
                            <a className="d-flex justify-content-center text-decoration-none" href="#" >
                                <button type="button" className="btn btn-danger">Lets Connects </button>
                            </a>
                        </div>
                    </div>
                </div>
            </section>
        <Message/>
        </main>
    );
}

export default Hero;