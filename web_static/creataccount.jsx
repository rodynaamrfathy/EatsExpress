import React from "react";
import { IconComponentNode } from "./IconComponentNode";
import { Line5 } from "./Line5";
import { Polygon1 } from "./Polygon1";
import { Vector } from "./Vector";
import { Vector1 } from "./Vector1";
import "./style.css";

export const CreateAccount = () => {
  return (
    <div className="create-account">
      <div className="create-an-acc-wrapper">
        <div className="create-an-acc">
          <div className="footer-safe-tour">
            <div className="div">
              <div className="company">
                <p className="text-wrapper">
                  Lan Yuan - Maadi
                  <br />
                  Planet Africa
                  <br />
                  Taboon
                  <br />
                  Hadrmout
                </p>
                <div className="text-wrapper-2">Restaurants</div>
              </div>
              <div className="travellers">
                <p className="text-wrapper">
                  Masaken El Rehab
                  <br />
                  Salah ElDin Street
                  <br />
                  Shabab El Mosalas
                  <br />
                  Sharea&#39; El Khawaga
                </p>
                <div className="text-wrapper-2">Popular Areas</div>
              </div>
              <div className="resources">
                <div className="text-wrapper">
                  Italian
                  <br />
                  Mexican
                  <br />
                  Sandwiches
                  <br />
                  Japanese
                </div>
                <div className="text-wrapper-2">Popular Cuisines</div>
              </div>
            </div>
            <p className="eats-express">
              <span className="span">EatsExpress</span>
              <span className="text-wrapper-3">.</span>
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
                  <span className="text-wrapper-4">
                    Feel free to get in touch with us vai email
                    <br />
                  </span>
                  <span className="text-wrapper-5">customersupport@eatsexpress.com</span>
                </p>
                <div className="text-wrapper-2">Get in Touch</div>
              </div>
            </div>
            <Line5 className="line" />
          </div>
          <div className="overlap">
            <div className="navigation">
              <div className="logo">
                <p className="p">
                  <span className="span">EatsExpress</span>
                  <span className="text-wrapper-3">.</span>
                </p>
              </div>
            </div>
            <div className="create-acc">
              <div className="overlap-group">
                <div className="rewrite-email">
                  <div className="div-wrapper">
                    <div className="text-wrapper-6">Rewrite your emai</div>
                  </div>
                </div>
                <div className="email">
                  <div className="div-wrapper">
                    <div className="text-wrapper-7">Email</div>
                  </div>
                </div>
                <div className="phone-numer">
                  <div className="overlap-2">
                    <div className="text-wrapper-8">Phone Number</div>
                  </div>
                </div>
                <div className="country-code">
                  <div className="overlap-3">
                    <div className="text-wrapper-9">Country code</div>
                    <Polygon1 className="polygon" />
                  </div>
                </div>
                <div className="firstname">
                  <div className="overlap-4">
                    <div className="base" />
                    <div className="text-wrapper-10">Firstname</div>
                  </div>
                </div>
                <div className="password">
                  <div className="overlap-4">
                    <div className="base" />
                    <div className="text-wrapper-10">Password</div>
                  </div>
                </div>
                <div className="overlap-wrapper">
                  <div className="overlap-4">
                    <div className="base" />
                    <div className="text-wrapper-10">username</div>
                  </div>
                </div>
                <div className="lastname">
                  <div className="overlap-4">
                    <div className="base" />
                    <div className="text-wrapper-10">Lastname</div>
                  </div>
                </div>
              </div>
              <div className="base-2" />
            </div>
            <button className="button">
              <div className="overlap-5">
                <div className="text-wrapper-11">Register</div>
              </div>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};