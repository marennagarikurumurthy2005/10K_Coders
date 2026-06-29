async function getProducts() {

    try {

        const res = await fetch(
            "https://fakestoreapi.com/products"
        );

        const products = await res.json();

        const container =
            document.getElementById("products-container");

        container.style.display = "flex";
        container.style.flexWrap = "wrap";
        container.style.gap = "20px";

        products.forEach(product => {

            const card = document.createElement("div");

            card.style.width = "250px";
            card.style.border = "1px solid black";
            card.style.padding = "10px";
            card.style.cursor = "pointer";

            const image = document.createElement("img");
            image.src = product.image;
            image.style.width = "100%";
            image.style.height = "200px";
            image.style.objectFit = "contain";

            const title = document.createElement("h3");
            title.textContent = product.title;

            card.appendChild(image);
            card.appendChild(title);

            container.appendChild(card);

            // card.addEventListener("click", () => {
            //     window.location.href =
            //     `single.html?id=${product.id}`;



        



// });


        card.addEventListener('click',()=>{
            window.location.href=`single.html?id=${product.id}`
        })

        });

    } catch (error) {
        console.log(error);
    }
}

getProducts();