import React from "react";
import "./style.css";

export const ViewCart = () => {
  return (
    <div className="view-cart">
      <div className="view-basket-wrapper">
        <div className="view-basket">
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
            </div>
          </div>
          <button className="button">
            <div className="overlap">
              <div className="text-wrapper-2">Complete order</div>
            </div>
          </button>
          <div className="cart">
            <img className="img" alt="Image" src="image-897.png" />
            <div className="text-wrapper-3">Cart</div>
          </div>
          <div className="overlap-2">
            <div className="card">
              <img className="base" alt="Base" src="base.png" />
              <div className="quantity">
                <div className="overlap-3">
                  <div className="text-wrapper-4">1</div>
                  <div className="text-wrapper-5">Quantity:</div>
                </div>
                <div className="group">
                  <div className="div-wrapper">
                    <div className="text-wrapper-6">+</div>
                  </div>
                </div>
                <div className="overlap-wrapper">
                  <div className="div-wrapper">
                    <div className="text-wrapper-7">-</div>
                  </div>
                </div>
              </div>
            </div>
            <div className="details">
              <div className="overlap-4">
                <p className="p">Add on 1, add on 2</p>
                <p className="text-wrapper-8">
                  The flavors of ranch dressing, chicken and our special pizza double cheese.
                </p>
                <div className="text-wrapper-9">Add ons</div>
              </div>
              <div className="text-wrapper-10">Item name</div>
            </div>
          </div>
          <div className="overlap-5">
            <div className="card-2">
              <div className="overlap-6">
                <img className="base-2" alt="Base" src="base.png" />
                <div className="details-2">
                  <div className="overlap-4">
                    <p className="p">Add on 1, add on 2</p>
                    <p className="text-wrapper-8">
                      The flavors of ranch dressing, chicken and our special pizza double cheese.
                    </p>
                    <div className="text-wrapper-9">Add ons</div>
                  </div>
                  <div className="text-wrapper-10">Item name</div>
                </div>
              </div>
              <div className="quantity-2">
                <div className="overlap-3">
                  <div className="text-wrapper-4">1</div>
                  <div className="text-wrapper-5">Quantity:</div>
                </div>
                <div className="group">
                  <div className="div-wrapper">
                    <div className="text-wrapper-6">+</div>
                  </div>
                </div>
                <div className="overlap-wrapper">
                  <div className="div-wrapper">
                    <div className="text-wrapper-7">-</div>
                  </div>
                </div>
              </div>
            </div>
            <img className="card-3" alt="Card" src="card-1.png" />
          </div>
        </div>
      </div>
    </div>
  );
};