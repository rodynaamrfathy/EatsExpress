import React from "react";
import { IconComponentNode } from "./IconComponentNode";
import { Item4 } from "./Item4";
import { Item6 } from "./Item6";
import { Item7 } from "./Item7";
import { Item8 } from "./Item8";
import "./style.css";

export const ConfirmOrder = () => {
  return (
    <div className="confirm-order">
      <div className="confirm-order-wrapper">
        <div className="div">
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
              <div className="text-wrapper-2">Hello, Rodyna!</div>
            </div>
          </div>
          <div className="overlap">
            <div className="amount">
              <div className="flexcontainer-wrapper">
                <div className="flexcontainer">
                  <p className="text">
                    <span className="text-wrapper-3">
                      Total <br />
                    </span>
                  </p>
                  <p className="text">
                    <span className="text-wrapper-3">Amount</span>
                  </p>
                </div>
              </div>
            </div>
            <div className="time">
              <div className="div-wrapper">
                <div className="flexcontainer-2">
                  <p className="text">
                    <span className="text-wrapper-3">
                      Estimated
                      <br />
                    </span>
                  </p>
                  <p className="text">
                    <span className="text-wrapper-3">Delivery Time </span>
                  </p>
                </div>
              </div>
            </div>
            <div className="order-summary">
              <div className="overlap-2">
                <div className="base" />
                <div className="text-wrapper-4">order summary</div>
                <Item4 className="line" />
                <div className="item">
                  <Item4 className="item-4" />
                  <div className="details">
                    <div className="text-wrapper-5">Item name</div>
                    <p className="qty">
                      <span className="text-wrapper-6">Qty:</span>
                    </p>
                    <div className="text-wrapper-7">Price:</div>
                    <div className="text-wrapper-8">$100</div>
                    <div className="text-wrapper-9">1</div>
                  </div>
                </div>
                <div className="item-2">
                  <Item4 className="item-4-instance" />
                  <div className="details">
                    <div className="text-wrapper-5">Item name</div>
                    <p className="qty">
                      <span className="text-wrapper-6">Qty:</span>
                    </p>
                    <div className="text-wrapper-7">Price:</div>
                    <div className="text-wrapper-8">$100</div>
                    <div className="text-wrapper-9">1</div>
                  </div>
                </div>
                <div className="item-3">
                  <div className="details-2">
                    <div className="text-wrapper-5">Item name</div>
                    <p className="qty">
                      <span className="text-wrapper-6">Qty:</span>
                    </p>
                    <div className="text-wrapper-7">Price:</div>
                    <div className="text-wrapper-8">$100</div>
                    <div className="text-wrapper-9">1</div>
                  </div>
                  <Item4 className="icon-instance-node" />
                </div>
                <div className="item-5">
                  <Item4 className="item-6" />
                  <div className="details">
                    <div className="text-wrapper-5">Item name</div>
                    <p className="qty">
                      <span className="text-wrapper-6">Qty:</span>
                    </p>
                    <div className="text-wrapper-7">Price:</div>
                    <div className="text-wrapper-8">$100</div>
                    <div className="text-wrapper-9">1</div>
                  </div>
                </div>
                <div className="item-7">
                  <div className="details-3">
                    <div className="text-wrapper-5">Item name</div>
                    <p className="qty">
                      <span className="text-wrapper-6">Qty:</span>
                    </p>
                    <div className="text-wrapper-7">Price:</div>
                    <div className="text-wrapper-8">$100</div>
                    <div className="text-wrapper-9">1</div>
                  </div>
                  <Item6 className="item-6-instance" />
                </div>
                <div className="item-8">
                  <Item7 className="item-7-instance" />
                  <div className="details-3">
                    <div className="text-wrapper-5">Item name</div>
                    <p className="qty">
                      <span className="text-wrapper-6">Qty:</span>
                    </p>
                    <div className="text-wrapper-7">Price:</div>
                    <div className="text-wrapper-8">$100</div>
                    <div className="text-wrapper-9">1</div>
                  </div>
                </div>
                <div className="item-9">
                  <IconComponentNode className="item-10" />
                  <Item8 className="item-8-instance" />
                  <div className="details-4">
                    <div className="text-wrapper-5">Item name</div>
                    <p className="qty">
                      <span className="text-wrapper-6">Qty:</span>
                    </p>
                    <div className="text-wrapper-7">Price:</div>
                    <div className="text-wrapper-8">$100</div>
                    <div className="text-wrapper-9">1</div>
                  </div>
                </div>
                <div className="details-wrapper">
                  <div className="details-5">
                    <div className="text-wrapper-5">Item name</div>
                    <p className="qty">
                      <span className="text-wrapper-6">Qty:</span>
                    </p>
                    <div className="text-wrapper-7">Price:</div>
                    <div className="text-wrapper-8">$100</div>
                    <div className="text-wrapper-9">1</div>
                  </div>
                </div>
              </div>
            </div>
            <div className="text-wrapper-10">12:05 - 12:20</div>
            <div className="flexcontainer-3">
              <p className="span-wrapper">
                <span className="text-wrapper-11">
                  30 <br />
                </span>
              </p>
              <p className="span-wrapper">
                <span className="text-wrapper-11">
                  <br />
                </span>
              </p>
              <p className="span-wrapper">
                <span className="text-wrapper-11">min</span>
              </p>
            </div>
            <div className="text-wrapper-12">Total : $3000</div>
            <div className="text-wrapper-13">$2850</div>
            <div className="text-wrapper-14">$150</div>
            <div className="text-wrapper-15">Taxes</div>
          </div>
          <button className="button">
            <div className="overlap-3">
              <div className="text-wrapper-16">Confirm order</div>
            </div>
          </button>
          <div className="address">
            <div className="overlap-4">
              <div className="overlap-5">
                <div className="saved-address">
                  <div className="overlap-group-2">
                    <div className="ellipse" />
                    <div className="text-wrapper-17">Address summary</div>
                  </div>
                </div>
                <p className="p">choose address from saved or type a new address</p>
              </div>
              <div className="overlap-wrapper">
                <div className="overlap-group-2">
                  <div className="text-wrapper-18">Address summary</div>
                  <div className="ellipse-2" />
                </div>
              </div>
              <div className="new-address">
                <div className="overlap-6">
                  <div className="base-2" />
                  <div className="text-wrapper-19">+ new address</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};