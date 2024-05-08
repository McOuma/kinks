import React from "react";
import lady from "../assets/images/lady.jpg"

function Hero() {
    return (
      <main>
        <div className="container">
          <div className="row">
            <div className="col-md-6">
              <img src={lady} alt="lady"/>
              <h1>Welcome to the first </h1>
            </div>
          </div>
          <h1>Welcome home</h1>
        </div>
        </main>
    );
}

export default Hero;