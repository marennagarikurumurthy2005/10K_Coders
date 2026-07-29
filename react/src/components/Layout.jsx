import React from "react";
import "./Layout.css";

const Layout = ({ inst }) => {
  return (
    <div className="card">
      <img
        src={inst.image}
        alt={inst.title}
        className="card-image"
      />

      <div className="card-content">
        <span className="category">{inst.category}</span>

        <h2 className="title">{inst.title}</h2>

        <p className="description">
          {inst.description.length > 100
            ? inst.description.slice(0, 100) + "..."
            : inst.description}
        </p>

        <div className="bottom">
          <span className="price">${inst.price}</span>

          <span className="rating">
            ⭐ {inst.rating.rate} ({inst.rating.count})
          </span>
        </div>

        <button className="btn">Add to Cart</button>
      </div>
    </div>
  );
};

export default Layout;