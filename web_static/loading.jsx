import React from "react";
import "styles/style.css";

export const Loading = () => {
  return (
    <div className="loading">
      <div className="loading-wrapper">
        <div className="div">
          <div className="navigation">
            <div className="logo">
              <p className="eats-express">
                <span className="text-wrapper">EatsExpress</span>
                <span className="span">.</span>
              </p>
            </div>
          </div>
          <div className="overlap">
            <div className="overlap-group">
              <div className="base" />
              <div className="base-2" />
              <div className="text-wrapper-2">time</div>
              <div className="text-wrapper-3">order summary</div>
            </div>
            <div className="div-wrapper">
              <div className="text-wrapper-4">Total ammount</div>
            </div>
          </div>
          <div className="overlap-group-2">
            <div className="text-wrapper-5">Confirm order</div>
          </div>
          <div className="overlap-2">
            <div className="text-wrapper-6">Loading...</div>
            <img className="image" alt="Image" src="images/other/Food Cover.png" />
          </div>
        </div>
      </div>
    </div>
  );
};