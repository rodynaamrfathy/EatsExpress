import React from "react";
import { IconComponentNode } from "./IconComponentNode";
import { Line5 } from "./Line5";
import { Vector } from "./Vector";
import { Vector1 } from "./Vector1";
import "./style.css";

export const Restaurant = () => {
  return (
    <div className="restaurant">
      <div className="resturant-wrapper">
        <div className="resturant">
          <div className="navigation">
            <div className="logo">
              <p className="eats-express">
                <span className="text-wrapper">EatsExpress</span>
                <span className="span">.</span>
              </p>
            </div>
          </div>
          <div className="account">
            <div className="overlap-group">
              <img className="image" alt="Image" src="image-894.png" />
              <div className="div">Hello, Rodyna!</div>
              <img className="img" alt="Image" src="image-895.png" />
            </div>
          </div>
          <div className="overlap">
            <div className="card">
              <img className="base" alt="Base" src="base.png" />
            </div>
            <div className="details">
              <div className="text-wrapper-2">Item name</div>
              <p className="p">The flavors of ranch dressing, chicken and our special pizza double cheese.</p>
            </div>
            <div className="overlap-wrapper">
              <div className="overlap-2">
                <div className="base-2" />
                <img className="base-3" alt="Base" src="base.png" />
                <div className="details-2">
                  <div className="text-wrapper-2">Item name</div>
                  <p className="p">The flavors of ranch dressing, chicken and our special pizza double cheese.</p>
                </div>
              </div>
            </div>
            <div className="overlap-group-wrapper">
              <div className="overlap-2">
                <div className="base-2" />
                <img className="base-3" alt="Base" src="base.png" />
                <div className="details-3">
                  <div className="text-wrapper-2">Item name</div>
                  <p className="p">The flavors of ranch dressing, chicken and our special pizza double cheese.</p>
                </div>
              </div>
            </div>
            <div className="div-wrapper">
              <div className="overlap-2">
                <div className="base-2" />
                <img className="base-3" alt="Base" src="base.png" />
                <div className="details-4">
                  <div className="text-wrapper-2">Item name</div>
                  <p className="p">The flavors of ranch dressing, chicken and our special pizza double cheese.</p>
                </div>
              </div>
            </div>
          </div>
          <div className="resturant-details">
            <div className="overlap-3">
              <img className="base-4" alt="Base" src="base.png" />
              <div className="text-wrapper-3">Restaurant name</div>
            </div>
          </div>
          <div className="footer-safe-tour">
            <div className="overlap-4">
              <div className="footer-safe-tour-2">
                <div className="company">
                  <p className="text-wrapper-4">
                    Lan Yuan - Maadi
                    <br />
                    Planet Africa
                    <br />
                    Taboon
                    <br />
                    Hadrmout
                  </p>
                  <div className="text-wrapper-5">Restaurants</div>
                </div>
                <div className="travellers">
                  <p className="text-wrapper-4">
                    Masaken El Rehab
                    <br />
                    Salah ElDin Street
                    <br />
                    Shabab El Mosalas
                    <br />
                    Sharea&#39; El Khawaga
                  </p>
                  <div className="text-wrapper-5">Popular Areas</div>
                </div>
                <div className="resources">
                  <div className="text-wrapper-4">
                    Italian
                    <br />
                    Mexican
                    <br />
                    Sandwiches
                    <br />
                    Japanese
                  </div>
                  <div className="text-wrapper-5">Popular Cuisines</div>
                </div>
              </div>
              <p className="eats-express-2">
                <span className="text-wrapper">EatsExpress</span>
                <span className="span">.</span>
              </p>
              <div className="frame">
                <div className="social">
                  <div className="group">
                    <Vector className="vector-instance" />
                  </div>
                  <div className="vector-wrapper">
                    <IconComponentNode className="icon-instance-node" />
                  </div>
                  <div className="vector-instance-wrapper">
                    <Vector1 className="vector-2" />
                  </div>
                </div>
                <div className="get-in-touch">
                  <p className="feel-free-to-get-in">
                    <span className="text-wrapper-6">
                      Feel free to get in touch with us vai email
                      <br />
                    </span>
                    <span className="text-wrapper-7">customersupport@eatsexpress.com</span>
                  </p>
                  <div className="text-wrapper-5">Get in Touch</div>
                </div>
              </div>
            </div>
            <Line5 className="line" />
          </div>
        </div>
      </div>
    </div>
  );
};