
async function getProduct() {

    const params =
        new URLSearchParams(window.location.search);

    const productId = params.get("id");

    const res = await fetch(
        `https://fakestoreapi.com/products/${productId}`
    );

    const product = await res.json();

    console.log(product);
}

getProduct();


async function getProduct() {

    const params =
        new URLSearchParams(window.location.search);

    const productId = params.get("id");

    const res = await fetch(
        `https://fakestoreapi.com/products/${productId}`
    );

    const product = await res.json();

    const container =
        document.getElementById("product");

    const image = document.createElement("img");
    image.src = product.image;
    image.style.width = "300px";

    const title = document.createElement("h2");
    title.textContent = product.title;

    const price = document.createElement("h3");
    price.textContent = `$${product.price}`;

    const description =
        document.createElement("p");
    description.textContent =
        product.description;

    container.append(
        image,
        title,
        price,
        description
    );
}

// getProduct();