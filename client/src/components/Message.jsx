import React from "react"
import ladyimage from '../assets/images/sa.jpg'
import ladies from "../assets/images/hairs.jpg"
import "./message.css"


function Message (){
    return(
        <main>
            <section className="info">
            <div className="information container">
                <p className="text-center fs-3 fw-medium text-danger ">Unleashing the Beauty of Afro Kinky Hair</p>
                <div className="justify-content-center">
                    <p>Welcome to Kinks and Queens, where we believe that every individual with Afro kinky hair has the power to explore, learn, and shine with their natural beauty. Our platform is dedicated to providing you with the knowledge, inspiration, and resources needed to embrace your unique hair texture and unleash your inner queen or king.</p>
                </div>
                <div className= "row">
                    <div className="col-md-6">
                        <p className="fs-4 fw-light text-danger text-center">Explore</p>
                        <p>Embark on a journey of exploration as we delve into the rich heritage and diverse styles of Afro kinky hair. From traditional braids and twists to trendy updos and protective hairstyles, we'll showcase a wide range of options for you to experiment with and express your personal style. Discover the beauty of different hair accessories, adornments, and colors that can complement and enhance your natural kinks.</p>
                        <p className="fs-4 fw-light text-danger text-center">Learn</p>
                        <p>Knowledge is power, and at Kinks and Queens, we're committed to educating and empowering you with valuable information about Afro kinky hair care, maintenance, and styling techniques. Our articles, tutorials, and expert tips will help you understand the unique characteristics of your hair, teach you how to properly care for and nurture your curls, and provide insights into the best products and practices for healthy and vibrant hair.</p>
                        <p className="fs-4 fw-light text-center text-danger">Shine</p>
                        <p> Your natural hair is a crown that deserves to shine brightly. We celebrate the beauty and versatility of Afro kinky hair and encourage you to embrace your uniqueness with confidence. Through inspiring stories, interviews with influencers and role models, and real-life experiences shared by our community, we aim to uplift and empower you to embrace your natural beauty and radiate with self-assurance.</p>
                    </div>
                    <div className=" col-md-6">
                        <img  src={ladyimage} alt="image" />
                    </div>
                </div>
            </div>
            </section>
            <section className="contact">
                <div className="my-contact container">
                    <div className="row">
                        <p className="fs-3 fw-bold text-center text-danger pb-5">Join Our Community</p>
                        <div className="col-md-6">
                            <img src={ladies} alt="pic"/>
                        </div>
                        <div className="col-md-6">
                            <p className="fs-4 fw-light text-center text-danger">Let's Connect</p>
                            <p>Join our community of kings and queens who are embracing their Afro kinky hair and shining with pride. Explore our content, learn from our experts, and let your natural beauty shine through. Remember, your hair is a reflection of your heritage, your culture, and your individuality, so embrace it, celebrate it, and let it be a source of inspiration for others.</p>
                            <p>At Kinks and Queens, we're more than just a platform – we're a support system, a source of inspiration, and a celebration of the magnificence of Afro kinky hair. So, come on in and let your natural beauty shine through. Together, let's explore, learn, and shine as the royalty we are.</p>
                            <a className=" d-flex text-decoration-none justify-content-center" href="" >
                                <button type="button" className="btn btn-danger">Subscribe</button>
                            </a>

                        </div>
                    </div>
                </div>
            </section>

        </main>
    )
}

export default Message