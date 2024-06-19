import React from "react";
import "./style.css";

export const AddItemToCart = () => {
  return (
    <div className="add-item-to-cart">
      <div className="order-wrapper">
        <div className="order">
          <div className="navigation">
            <div className="logo">
              <p className="eats-express">
                <span className="text-wrapper">EatsExpress</span>
                <span className="span">.</span>
              </p>
            </div>
          </div>
          <div className="group">
            <div className="overlap-group">
              <img className="image" alt="Image" src="image-897.png" />
              <img className="image" alt="Image" src="image-897.png" />
              <div className="div">Hello, Rodyna!</div>
              <img className="img" alt="Image" src="image-895.png" />
            </div>
          </div>
          <div className="overlap">
            <div className="overlap-2">
              <img className="base" alt="Base" src="base.png" />
              <div className="frame">
                <div className="text-wrapper-2">Item name</div>
                <p className="p">The flavors of ranch dressing, chicken and our special pizza double cheese.</p>
                <div className="text-wrapper-3">$100</div>
                <div className="text-wrapper-4">Add ons</div>
                <div className="frame-2">
                  <div className="overlap-3">
                    <div className="text-wrapper-5">1</div>
                    <div className="text-wrapper-6">Quantity:</div>
                  </div>
                  <div className="overlap-group-wrapper">
                    <div className="div-wrapper">
                      <div className="text-wrapper-7">-</div>
                    </div>
                  </div>
                  <div className="overlap-wrapper">
                    <div className="div-wrapper">
                      <div className="text-wrapper-8">+</div>
                    </div>
                  </div>
                </div>
                <div className="overlap-4">
                  <div className="add-on">
                    <div className="ellipse" />
                  </div>
                  <div className="add-on-2">
                    <div className="overlap-5">
                      <div className="ellipse-2" />
                      <div className="text-wrapper-9">add on 2</div>
                    </div>
                    <div className="text-wrapper-10">add on 3</div>
                  </div>
                </div>
                <div className="add-on-3">
                  <div className="overlap-6">
                    <div className="ellipse-3" />
                    <div className="text-wrapper-11">Add on 1</div>
                  </div>
                </div>
              </div>
            </div>
            <button className="button">
              <div className="overlap-7">
                <div className="text-wrapper-12">Add to cart</div>
              </div>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};