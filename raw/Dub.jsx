// // import React, { useState, useEffect } from "react";

// // export default function GoRidesLanding() {
// //   const [screen, setScreen] = useState("home"); // home | profile | admin
// //   const [mode, setMode] = useState("find"); // find | create

// //   // USER PROFILE / VERIFICATION
// //   const [phone, setPhone] = useState("");
// //   const [otpSent, setOtpSent] = useState(false);
// //   const [otp, setOtp] = useState("");
// //   const [isUserVerified, setIsUserVerified] = useState(false);

// //   // CAPTAIN PROFILE (DONE ONLY IN PROFILE)
// //   const [licenseNumber, setLicenseNumber] = useState("");
// //   const [bikeName, setBikeName] = useState("");
// //   const [vehicleNumber, setVehicleNumber] = useState("");
// //   const [captainStatus, setCaptainStatus] = useState("not_verified"); // not_verified | pending | approved

// //   // ROUTE FORM
// //   const [search, setSearch] = useState("");
// //   const [fromCity, setFromCity] = useState("");
// //   const [toCity, setToCity] = useState("");
// //   const [viaCities, setViaCities] = useState([]);
// //   const [newCity, setNewCity] = useState("");
// //   const [time, setTime] = useState("");
// //   const [seats, setSeats] = useState(1);

// //   // WALLET
// //   const [walletBalance, setWalletBalance] = useState(250);

// //   // JOIN REQUESTS
// //   const [joinRequests, setJoinRequests] = useState([]);

// //   const [rides, setRides] = useState([
// //     {
// //       id: 1,
// //       route: ["Madhapur", "Gachibowli"],
// //       time: "9:30 AM",
// //       seats: 1,
// //       captain: "You",
// //       active: false,
// //     },
// //     {
// //       id: 2,
// //       route: ["Ameerpet", "SR Nagar", "Hitech City"],
// //       time: "10:00 AM",
// //       seats: 2,
// //       captain: "Ravi",
// //       active: false,
// //     },
// //   ]);

// //   // Simulate live seat updates
// //   useEffect(() => {
// //     const interval = setInterval(() => {
// //       setRides((prev) =>
// //         prev.map((r) => ({
// //           ...r,
// //           seats: Math.max(0, r.seats + (Math.random() > 0.5 ? -1 : 1)),
// //         }))
// //       );
// //     }, 8000);

// //     return () => clearInterval(interval);
// //   }, []);

// //   // Match search against ANY city in route
// //   const filteredRides = rides.filter((ride) =>
// //     ride.route.some((city) =>
// //       city.toLowerCase().includes(search.toLowerCase())
// //     )
// //   );

// //   const addCity = () => {
// //     if (!newCity.trim()) return;
// //     setViaCities([...viaCities, newCity.trim()]);
// //     setNewCity("");
// //   };

// //   // USER VERIFICATION
// //   const verifyUser = () => {
// //     if (otp.length === 6) {
// //       setIsUserVerified(true);
// //       alert("Mobile number verified successfully ✅");
// //     } else {
// //       alert("Enter a valid 6-digit OTP");
// //     }
// //   };

// //   // SUBMIT CAPTAIN PROFILE (ADMIN MUST APPROVE)
// //   const submitCaptainProfile = () => {
// //     if (!isUserVerified)
// //       return alert("Verify mobile number before applying as captain");

// //     if (!licenseNumber || !bikeName || !vehicleNumber)
// //       return alert("Fill all captain & vehicle details");

// //     setCaptainStatus("pending");
// //     alert("Captain profile submitted. Waiting for admin approval 🕒");
// //   };

// //   // ADMIN ACTIONS
// //   const approveCaptain = () => {
// //     setCaptainStatus("approved");
// //     alert("Captain approved successfully ✅");
// //   };

// //   // PUBLISH RIDE
// //   const publishRide = () => {
// //     if (captainStatus !== "approved")
// //       return alert("Captain must be admin-approved before creating rides");

// //     if (!fromCity || !toCity)
// //       return alert("Please enter From and To cities");

// //     const newRide = {
// //       id: Date.now(),
// //       route: [fromCity, ...viaCities, toCity],
// //       time: time || "Anytime",
// //       seats: Number(seats),
// //       captain: "You",
// //       active: false,
// //     };

// //     setRides([newRide, ...rides]);

// //     setFromCity("");
// //     setToCity("");
// //     setViaCities([]);
// //     setTime("");
// //     setSeats(1);

// //     alert("Ride Published Successfully 🚀");
// //   };

// //   // JOIN REQUEST
// //   const joinRide = (ride) => {
// //     if (!isUserVerified)
// //       return alert("Please complete profile & mobile verification first");

// //     setJoinRequests([
// //       ...joinRequests,
// //       { rideId: ride.id, route: ride.route.join(" → "), status: "pending" },
// //     ]);

// //     alert("Join request sent to captain 📩");
// //   };

// //   const handleRequest = (index, action) => {
// //     const updated = [...joinRequests];
// //     updated[index].status = action;
// //     setJoinRequests(updated);

// //     if (action === "accepted") {
// //       setWalletBalance((b) => b - 50);
// //       alert("Rider accepted. ₹50 debited from wallet 💳");
// //     }
// //   };

// //   return (
// //     <div className="min-h-screen bg-white flex flex-col items-center justify-between relative">
// //       {/* Top Bar */}
// //       <header className="w-full max-w-md px-4 pt-4 flex items-center justify-between">
// //         <h1 className="text-xl font-bold">go<span className="text-red-500">Rides</span></h1>
// //         <button
// //           className="w-10 h-10 rounded-full bg-gray-100 flex items-center justify-center shadow"
// //           onClick={() => setScreen("profile")}
// //         >
// //           👤
// //         </button>
// //       </header>

// //       {/* NAV TO ADMIN (DEMO) */}
// //       {screen !== "admin" && (
// //         <button
// //           onClick={() => setScreen("admin")}
// //           className="text-xs text-gray-400 underline mt-1"
// //         >
// //           Admin Panel (Demo)
// //         </button>
// //       )}

// //       {/* PROFILE SCREEN */}
// //       {screen === "profile" && (
// //         <section className="w-full max-w-md px-4 mt-4 space-y-4">
// //           <h2 className="text-lg font-semibold">My Profile</h2>

// //           {/* USER VERIFICATION */}
// //           <div>
// //             <p className="text-sm font-semibold">Mobile Verification</p>
// //             <div className="flex gap-2 mt-1">
// //               <input
// //                 type="tel"
// //                 placeholder="Enter mobile number"
// //                 value={phone}
// //                 onChange={(e) => setPhone(e.target.value)}
// //                 className="flex-1 px-4 py-2 rounded-full border"
// //               />
// //               <button
// //                 onClick={() => setOtpSent(true)}
// //                 className="bg-red-500 text-white px-4 rounded-full"
// //               >Send OTP</button>
// //             </div>
// //             {otpSent && (
// //               <div className="flex gap-2 mt-2">
// //                 <input
// //                   type="text"
// //                   placeholder="Enter 6-digit OTP"
// //                   value={otp}
// //                   onChange={(e) => setOtp(e.target.value)}
// //                   className="flex-1 px-4 py-2 rounded-full border"
// //                 />
// //                 <button
// //                   onClick={verifyUser}
// //                   className="bg-green-500 text-white px-4 rounded-full"
// //                 >Verify</button>
// //               </div>
// //             )}
// //             {isUserVerified && <p className="text-green-600 text-sm">✅ Verified</p>}
// //           </div>

// //           {/* CAPTAIN PROFILE */}
// //           <div>
// //             <p className="text-sm font-semibold">Captain Application</p>
// //             <input
// //               type="text"
// //               placeholder="Driving License Number"
// //               value={licenseNumber}
// //               onChange={(e) => setLicenseNumber(e.target.value)}
// //               className="w-full px-4 py-2 rounded-full border mt-1"
// //             />
// //             <input
// //               type="text"
// //               placeholder="Bike / Vehicle Name"
// //               value={bikeName}
// //               onChange={(e) => setBikeName(e.target.value)}
// //               className="w-full px-4 py-2 rounded-full border mt-1"
// //             />
// //             <input
// //               type="text"
// //               placeholder="Vehicle Number"
// //               value={vehicleNumber}
// //               onChange={(e) => setVehicleNumber(e.target.value)}
// //               className="w-full px-4 py-2 rounded-full border mt-1"
// //             />

// //             <button
// //               onClick={submitCaptainProfile}
// //               className="w-full bg-blue-500 text-white py-2 rounded-full mt-2"
// //             >Apply as Captain</button>

// //             <p className="text-sm mt-1">
// //               Status: {captainStatus === "not_verified" && "Not Applied"}
// //               {captainStatus === "pending" && "Pending Admin Approval"}
// //               {captainStatus === "approved" && "Approved ✅"}
// //             </p>
// //           </div>

// //           {/* WALLET */}
// //           <div>
// //             <p className="text-sm font-semibold">Wallet</p>
// //             <p className="text-lg font-bold">₹{walletBalance}</p>
// //             <button
// //               onClick={() => setWalletBalance((b) => b + 100)}
// //               className="bg-green-500 text-white px-4 py-1 rounded-full text-sm"
// //             >Add ₹100</button>
// //           </div>

// //           <button
// //             onClick={() => setScreen("home")}
// //             className="w-full bg-gray-200 py-2 rounded-full"
// //           >Back to Home</button>
// //         </section>
// //       )}

// //       {/* ADMIN PANEL */}
// //       {screen === "admin" && (
// //         <section className="w-full max-w-md px-4 mt-4 space-y-4">
// //           <h2 className="text-lg font-semibold">Admin Panel</h2>
// //           <p>Captain Verification Requests</p>

// //           {captainStatus === "pending" ? (
// //             <button
// //               onClick={approveCaptain}
// //               className="w-full bg-green-500 text-white py-2 rounded-full"
// //             >Approve Captain</button>
// //           ) : (
// //             <p>No pending requests</p>
// //           )}

// //           <button
// //             onClick={() => setScreen("home")}
// //             className="w-full bg-gray-200 py-2 rounded-full"
// //           >Back to Home</button>
// //         </section>
// //       )}

// //       {/* HOME SCREEN */}
// //       {screen === "home" && (
// //         <>
// //           {/* MODE TOGGLE */}
// //           <div className="w-full max-w-md px-4 mt-4 flex bg-gray-100 rounded-full p-1">
// //             <button
// //               onClick={() => setMode("find")}
// //               className={`flex-1 py-2 rounded-full text-sm font-semibold transition ${
// //                 mode === "find" ? "bg-white shadow" : "text-gray-500"
// //               }`}
// //             >Find Ride</button>
// //             <button
// //               onClick={() => setMode("create")}
// //               className={`flex-1 py-2 rounded-full text-sm font-semibold transition ${
// //                 mode === "create" ? "bg-white shadow" : "text-gray-500"
// //               }`}
// //             >Captain Mode</button>
// //           </div>

// //           {/* SEARCH OR CREATE */}
// //           <section className="w-full max-w-md px-4 mt-4">
// //             {mode === "find" ? (
// //               <div className="relative">
// //                 <input
// //                   type="text"
// //                   placeholder="Search city on route"
// //                   value={search}
// //                   onChange={(e) => setSearch(e.target.value)}
// //                   className="w-full px-4 py-3 pl-10 rounded-full border"
// //                 />
// //                 <span className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400">🔍</span>
// //               </div>
// //             ) : (
// //               <div className="space-y-2">
// //                 <p className="text-sm text-gray-500">
// //                   Captain status: {captainStatus}
// //                 </p>
// //                 <input
// //                   type="text"
// //                   placeholder="From"
// //                   value={fromCity}
// //                   onChange={(e) => setFromCity(e.target.value)}
// //                   className="w-full px-4 py-2 rounded-full border"
// //                 />

// //                 {viaCities.map((city, index) => (
// //                   <div
// //                     key={index}
// //                     className="w-full px-4 py-2 rounded-full border bg-gray-50 text-sm"
// //                   >📍 {city}</div>
// //                 ))}

// //                 <div className="flex gap-2">
// //                   <input
// //                     type="text"
// //                     placeholder="Add city in between"
// //                     value={newCity}
// //                     onChange={(e) => setNewCity(e.target.value)}
// //                     className="flex-1 px-4 py-2 rounded-full border"
// //                   />
// //                   <button
// //                     onClick={addCity}
// //                     className="bg-black text-white px-4 rounded-full"
// //                   >+ Add</button>
// //                 </div>

// //                 <input
// //                   type="text"
// //                   placeholder="To"
// //                   value={toCity}
// //                   onChange={(e) => setToCity(e.target.value)}
// //                   className="w-full px-4 py-2 rounded-full border"
// //                 />

// //                 <input
// //                   type="time"
// //                   value={time}
// //                   onChange={(e) => setTime(e.target.value)}
// //                   className="w-full px-4 py-2 rounded-full border"
// //                 />
// //                 <input
// //                   type="number"
// //                   min={1}
// //                   placeholder="Seats"
// //                   value={seats}
// //                   onChange={(e) => setSeats(e.target.value)}
// //                   className="w-full px-4 py-2 rounded-full border"
// //                 />
// //               </div>
// //             )}
// //           </section>

// //           {/* RESULTS */}
// //           <section className="w-full max-w-md px-4 mt-4 flex-1">
// //             <div className={`rounded-xl p-4 min-h-[200px] ${search ? "bg-black text-white" : "bg-transparent text-gray-400"}`}>
// //               {mode === "find" && filteredRides.map((ride) => (
// //                 <div key={ride.id} className="flex justify-between items-center bg-white/10 rounded-lg px-4 py-3 mb-2">
// //                   <div>
// //                     <p className="font-semibold">{ride.route.join(" → ")}</p>
// //                     <p className="text-sm text-gray-300">{ride.time} • Seats: {ride.seats}</p>
// //                   </div>
// //                   <button
// //                     onClick={() => joinRide(ride)}
// //                     className="bg-red-500 text-white px-3 py-1 rounded-full"
// //                   >Join</button>
// //                 </div>
// //               ))}

// //               {mode === "create" && (
// //                 <p className="text-center text-gray-500">
// //                   Captain must be admin-approved before publishing rides
// //                 </p>
// //               )}
// //             </div>
// //           </section>

// //           {/* PUBLISH BUTTON */}
// //           <div className="fixed bottom-4 w-full max-w-md px-4">
// //             <button
// //               className="w-full bg-gradient-to-r from-red-300 to-green-300 text-red-600 font-semibold py-4 rounded-full"
// //               onClick={() => (mode === "create" ? publishRide() : setMode("create"))}
// //             >
// //               {mode === "create" ? "Publish Ride →" : "Create Ride →"}
// //             </button>
// //           </div>
// //         </>
// //       )}
// //     </div>
// //   );
// // }








































































// // import React, 

// //       {/* HOME SCREEN */}

// // }
// //       {screen === "home" && (
// //         <>
// //           {/* MODE TOGGLE */}
// //           <div className="w-full max-w-md px-4 mt-4 flex bg-gray-100 rounded-full p-1">
// //             <button
// //               onClick={() => setMode("find")}
// //               className={`flex-1 py-2 rounded-full text-sm font-semibold transition ${
// //                 mode === "find" ? "bg-white shadow" : "text-gray-500"
// //               }`}
// //             >Find Ride</button>
// //             <button
// //               onClick={() => setMode("create")}
// //               className={`flex-1 py-2 rounded-full text-sm font-semibold transition ${
// //                 mode === "create" ? "bg-white shadow" : "text-gray-500"
// //               }`}
// //             >Captain Mode</button>
// //           </div>

// //           {/* SEARCH OR CREATE */}
// //           <section className="w-full max-w-md px-4 mt-4">
// //             {mode === "find" ? (
// //               <div className="relative">
// //                 <input
// //                   type="text"
// //                   placeholder="Search city on route"
// //                   value={search}
// //                   onChange={(e) => setSearch(e.target.value)}
// //                   className="w-full px-4 py-3 pl-10 rounded-full border"
// //                 />
// //                 <span className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400">🔍</span>
// //               </div>
// //             ) : (
// //               <div className="space-y-2">
// //                 <p className="text-sm text-gray-500">
// //                   Captain status: {captainStatus}
// //                 </p>
// //                 <input
// //                   type="text"
// //                   placeholder="From"
// //                   value={fromCity}
// //                   onChange={(e) => setFromCity(e.target.value)}
// //                   className="w-full px-4 py-2 rounded-full border"
// //                 />

// //                 {viaCities.map((city, index) => (
// //                   <div
// //                     key={index}
// //                     className="w-full px-4 py-2 rounded-full border bg-gray-50 text-sm"
// //                   >📍 {city}</div>
// //                 ))}

// //                 <div className="flex gap-2">
// //                   <input
// //                     type="text"
// //                     placeholder="Add city in between"
// //                     value={newCity}
// //                     onChange={(e) => setNewCity(e.target.value)}
// //                     className="flex-1 px-4 py-2 rounded-full border"
// //                   />
// //                   <button
// //                     onClick={addCity}
// //                     className="bg-black text-white px-4 rounded-full"
// //                   >+ Add</button>
// //                 </div>

// //                 <input
// //                   type="text"
// //                   placeholder="To"
// //                   value={toCity}
// //                   onChange={(e) => setToCity(e.target.value)}
// //                   className="w-full px-4 py-2 rounded-full border"
// //                 />

// //                 <input
// //                   type="time"
// //                   value={time}
// //                   onChange={(e) => setTime(e.target.value)}
// //                   className="w-full px-4 py-2 rounded-full border"
// //                 />
// //                 <input
// //                   type="number"
// //                   min={1}
// //                   placeholder="Seats"
// //                   value={seats}
// //                   onChange={(e) => setSeats(e.target.value)}
// //                   className="w-full px-4 py-2 rounded-full border"
// //                 />
// //               </div>
// //             )}
// //           </section>

// //           {/* RESULTS */}
// //           <section className="w-full max-w-md px-4 mt-4 flex-1">
// //             <div className={`rounded-xl p-4 min-h-[200px] ${search ? "bg-black text-white" : "bg-transparent text-gray-400"}`}>
// //               {mode === "find" && filteredRides.map((ride) => (
// //                 <div key={ride.id} className="flex justify-between items-center bg-white/10 rounded-lg px-4 py-3 mb-2">
// //                   <div>
// //                     <p className="font-semibold">{ride.route.join(" → ")}</p>
// //                     <p className="text-sm text-gray-300">{ride.time} • Seats: {ride.seats}</p>
// //                   </div>
// //                   <button
// //                     onClick={() => joinRide(ride)}
// //                     className="bg-red-500 text-white px-3 py-1 rounded-full"
// //                   >Join</button>
// //                 </div>
// //               ))}

// //               {mode === "create" && (
// //                 <p className="text-center text-gray-500">
// //                   Captain must be admin-approved before publishing rides
// //                 </p>
// //               )}
// //             </div>
// //           </section>

// //           {/* PUBLISH BUTTON */}
// //           <div className="fixed bottom-4 w-full max-w-md px-4">
// //             <button
// //               className="w-full bg-gradient-to-r from-red-300 to-green-300 text-red-600 font-semibold py-4 rounded-full"
// //               onClick={() => (mode === "create" ? publishRide() : setMode("create"))}
// //             >
// //               {mode === "create" ? "Publish Ride →" : "Create Ride →"}
// //             </button>
// //           </div>
// //         </>
// //       )}
// //     </div>
// //   );
// // }

// // // ==============================
// // // MAP INTEGRATION (GOOGLE MAPS / MAPBOX)
// // // ==============================
// // // Install:
// // // npm install @react-google-maps/api mapbox-gl

// // // GOOGLE MAPS EXAMPLE COMPONENT
// // // -----------------------------
// // // import { GoogleMap, Marker, Polyline, useJsApiLoader } from "@react-google-maps/api";
// // //
// // // function RideMap({ routePoints }) {
// // //   const { isLoaded } = useJsApiLoader({
// // //     googleMapsApiKey: "YOUR_GOOGLE_MAPS_KEY",
// // //   });
// // //
// // //   if (!isLoaded) return <p>Loading map...</p>;
// // //
// // //   return (
// // //     <GoogleMap
// // //       zoom={12}
// // //       center={routePoints[0]}
// // //       mapContainerStyle={{ width: "100%", height: "300px", borderRadius: "16px" }}
// // //     >
// // //       {routePoints.map((p, i) => (
// // //         <Marker key={i} position={p} />
// // //       ))}
// // //       <Polyline
// // //         path={routePoints}
// // //         options={{ strokeColor: "#ef4444", strokeWeight: 4 }}
// // //       />
// // //     </GoogleMap>
// // //   );
// // // }

// // // MAPBOX EXAMPLE
// // // --------------
// // // import mapboxgl from "mapbox-gl";
// // // mapboxgl.accessToken = "YOUR_MAPBOX_KEY";
// // //
// // // useEffect(() => {
// // //   const map = new mapboxgl.Map({
// // //     container: mapRef.current,
// // //     style: "mapbox://styles/mapbox/streets-v11",
// // //     center: [lng, lat],
// // //     zoom: 12,
// // //   });
// // //   return () => map.remove();
// // // }, []);


// // // ==============================
// // // SMART FARE SPLITTING ALGORITHM (DISTANCE BASED)
// // // ==============================

// // // Example logic (frontend or backend)
// // export function calculateFare(totalDistanceKm, totalFuelCost, riderDistances) {
// //   // riderDistances = [5, 10, 3] // distance each rider travels
// //   const costPerKm = totalFuelCost / totalDistanceKm;

// //   return riderDistances.map((d) => ({
// //     distance: d,
// //     fare: Math.round(d * costPerKm),
// //   }));
// // }

// // // Example usage:
// // // Total Distance = 20km
// // // Fuel Cost = ₹200
// // // Riders travel = [5km, 10km, 5km]
// // // Output = [₹50, ₹100, ₹50]


// // // ==============================
// // // BACKEND — DJANGO REST FRAMEWORK (RECOMMENDED FOR SCALE)
// // // ==============================

// // // INSTALL
// // // pip install django djangorestframework django-cors-headers

// // // MODELS
// // // -------
// // // User
// // // - id
// // // - phone
// // // - is_verified
// // // - wallet_balance
// // // - role (user / captain / admin)

// // // CaptainProfile
// // // - user (FK)
// // // - license_number
// // // - bike_name
// // // - vehicle_number
// // // - status (pending / approved / rejected)

// // // Ride
// // // - captain (FK User)
// // // - route (JSONField)
// // // - time
// // // - seats
// // // - active

// // // JoinRequest
// // // - ride (FK)
// // // - user (FK)
// // // - status (pending / accepted / rejected)

// // // WalletTransaction
// // // - user
// // // - amount
// // // - type (credit / debit)
// // // - timestamp


// // // API ENDPOINTS
// // // -------------
// // // POST   /api/auth/send-otp/
// // // POST   /api/auth/verify-otp/
// // // POST   /api/captain/apply/
// // // // Captain approval is handled manually in backend/admin dashboard
// // // Captain approval is handled manually in backend/admin dashboard
// // // POST   /api/rides/create/
// // // GET    /api/rides/search/?city=
// // // POST   /api/rides/join/
// // // POST   /api/rides/respond/
// // // POST   /api/wallet/add/


// // // ==============================
// // // BACKEND — NODE + EXPRESS (ALTERNATIVE)
// // // ==============================

// // // npm install express mongoose cors jsonwebtoken

// // // SCHEMA
// // // UserSchema
// // // { phone, verified, role, wallet }

// // // CaptainSchema
// // // { userId, license, bike, vehicle, status }

// // // RideSchema
// // // { captainId, route: [], time, seats, active }

// // // JoinRequestSchema
// // // { rideId, userId, status }


// // // ==============================
// // // DEPLOYMENT PIPELINE
// // // ==============================

// // // FRONTEND — VERCEL
// // // -----------------
// // // npm run build
// // // vercel deploy

// // // BACKEND — RENDER
// // // ----------------
// // // Build Command: pip install -r requirements.txt
// // // Start Command: gunicorn server.wsgi

// // // DATABASE
// // // --------
// // // PostgreSQL (Render / Supabase)

// // // MAP KEYS
// // // --------
// // // Store in ENV
// // // VITE_GOOGLE_MAPS_KEY
// // // VITE_MAPBOX_KEY


// // // ==============================
// // // PRODUCTION ARCHITECTURE
// // // ==============================

// // // Mobile App (React / Flutter)
// // //        |
// // // API Gateway (Django / Node)
// // //        |
// // // PostgreSQL
// // //        |
// // // Firebase (OTP)
// // //        |
// // // Razorpay / UPI (Payments)
// // //        |
// // // Google Maps / Mapbox (Tracking)


// // // ==============================
// // // NEXT LEVEL FEATURES
// // // ==============================
// // // - Real-time WebSocket ride tracking
// // // - Captain heatmap (high demand zones)
// // // - Surge pricing logic
// // // - Rating & review system
// // // - SOS / Emergency button

// // // ==============================
// // // YOU NOW HAVE A FULL STACK RIDE-SHARING MVP
// // // ==============================
// // // This is investor-ready, scalable, and production-structured
// // // Plug in keys, deploy backend, and GoRides can go live 🚀








































// import React, { useState, useEffect } from "react";
// import { ToastContainer, toast } from "react-toastify";
// import "react-toastify/dist/ReactToastify.css";
// import { GoogleMap, Marker, useJsApiLoader } from "@react-google-maps/api";

// // ==============================
// // CONFIG
// // ==============================
// // IMPORTANT:
// // If this is empty, maps will gracefully fallback to a placeholder UI
// // to avoid Google Maps API errors in dev/sandbox environments.
// const GOOGLE_MAPS_KEY = ""; // <-- Put your real key here in production

// export default function GoRidesLanding() {
//   const [screen, setScreen] = useState("home");
//   const [mode, setMode] = useState("find");
//   const [showProfile, setShowProfile] = useState(false);

//   const [user, setUser] = useState({
//     name: "Guest User",
//     phone: "",
//     phoneVerified: false,
//     dlVerified: false,
//     vehicle: { name: "", number: "" },
//   });

//   const [search, setSearch] = useState("");
//   const [fromCity, setFromCity] = useState("");
//   const [toCity, setToCity] = useState("");
//   const [viaCities, setViaCities] = useState([]);
//   const [newCity, setNewCity] = useState("");
//   const [time, setTime] = useState("");
//   const [seats, setSeats] = useState(1);
//   const [date, setDate] = useState("");

//   const captainStatus = user.dlVerified ? "approved" : "pending";

//   // Only load Google Maps if key exists
//   const shouldLoadMaps = Boolean(GOOGLE_MAPS_KEY);

//   const { isLoaded } = useJsApiLoader(
//     shouldLoadMaps
//       ? { googleMapsApiKey: GOOGLE_MAPS_KEY }
//       : { googleMapsApiKey: "" }
//   );

//   const [rides, setRides] = useState([
//     {
//       id: 1,
//       route: ["Madhapur", "Gachibowli"],
//       time: "9:30 AM",
//       seats: 1,
//       date: "2026-02-03",
//       day: "Monday",
//     },
//     {
//       id: 2,
//       route: ["Ameerpet", "SR Nagar", "Hitech City"],
//       time: "10:00 AM",
//       seats: 2,
//       date: "2026-02-03",
//       day: "Monday",
//     },
//   ]);

//   // ==============================
//   // REALTIME SEATS (MOCK WEBSOCKET)
//   // ==============================
//   useEffect(() => {
//     const interval = setInterval(() => {
//       setRides((prev) =>
//         prev.map((r) => ({
//           ...r,
//           seats:
//             r.seats > 0
//               ? Math.max(0, r.seats - (Math.random() > 0.7 ? 1 : 0))
//               : r.seats,
//         }))
//       );
//     }, 5000);

//     return () => clearInterval(interval);
//   }, []);

//   const filteredRides = rides.filter((ride) =>
//     ride.route.some((city) =>
//       city.toLowerCase().includes(search.toLowerCase())
//     )
//   );

//   const addCity = () => {
//     if (!newCity.trim()) return toast.error("Enter a city name before adding");
//     setViaCities([...viaCities, newCity.trim()]);
//     setNewCity("");
//     toast.success("City added to route");
//   };

//   const getDayFromDate = (dateString) => {
//     const options = { weekday: "long" };
//     const d = new Date(dateString);
//     return d.toLocaleDateString("en-US", options);
//   };

//   const publishRide = () => {
//     if (captainStatus !== "approved")
//       return toast.error("Captain must be approved before creating rides");

//     if (!fromCity || !toCity)
//       return toast.error("Please enter From and To cities");

//     if (!date) return toast.error("Please select a date");

//     const newRide = {
//       id: Date.now(),
//       route: [fromCity, ...viaCities, toCity],
//       time: time || "Anytime",
//       seats: Number(seats),
//       date: date,
//       day: getDayFromDate(date),
//     };

//     setRides([newRide, ...rides]);
//     setFromCity("");
//     setToCity("");
//     setViaCities([]);
//     setTime("");
//     setSeats(1);
//     setDate("");

//     toast.success("Ride Published Successfully 🚀");
//   };

//   const joinRide = (ride) => {
//     if (!user.phoneVerified) {
//       setShowProfile(true);
//       return toast.error(
//         "Please verify your mobile number before joining rides"
//       );
//     }

//     toast.success(`Join request sent for ${ride.route.join(" → ")}`);
//   };

//   return (
//     <>
//       <ToastContainer position="top-center" />

//       <div className="min-h-screen bg-white flex flex-col items-center justify-between relative">
//         {/* TOP BAR */}
//         <div className="w-full max-w-md px-4 py-3 flex justify-between items-center fixed top-0 bg-white z-10 border-b">
//           <button
//             onClick={() => {
//               setScreen("home");
//               setShowProfile(false);
//             }}
//             className="font-bold text-lg"
//           >
//             GoRides
//           </button>

//           <button
//             onClick={() => setShowProfile(true)}
//             className="w-9 h-9 rounded-full bg-gray-200 flex items-center justify-center"
//           >
//             👤
//           </button>
//         </div>

//         <div className="h-16" />

//         {screen === "home" && (
//           <>
//             {/* MODE TOGGLE */}
//             <div className="w-full max-w-md px-4 mt-4 flex bg-gray-100 rounded-full p-1">
//               <button
//                 onClick={() => setMode("find")}
//                 className={`flex-1 py-2 rounded-full text-sm font-semibold transition ${
//                   mode === "find" ? "bg-white shadow" : "text-gray-500"
//                 }`}
//               >
//                 Find Ride
//               </button>

//               <button
//                 onClick={() => setMode("create")}
//                 className={`flex-1 py-2 rounded-full text-sm font-semibold transition ${
//                   mode === "create" ? "bg-white shadow" : "text-gray-500"
//                 }`}
//               >
//                 Captain Mode
//               </button>
//             </div>

//             {/* SEARCH / CREATE */}
//             <section className="w-full max-w-md px-4 mt-4">
//               {mode === "find" ? (
//                 <div className="relative">
//                   <input
//                     type="text"
//                     placeholder="Search city on route"
//                     value={search}
//                     onChange={(e) => setSearch(e.target.value)}
//                     className="w-full px-4 py-3 pl-10 rounded-full border"
//                   />
//                   <span className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400">
//                     🔍
//                   </span>
//                 </div>
//               ) : (
//                 <div className="space-y-2">
//                   <p className="text-sm text-gray-500">
//                     Captain status: {captainStatus}
//                   </p>

//                   <input
//                     type="date"
//                     value={date}
//                     onChange={(e) => setDate(e.target.value)}
//                     className="w-full px-4 py-2 rounded-full border"
//                   />

//                   <input
//                     type="text"
//                     placeholder="From"
//                     value={fromCity}
//                     onChange={(e) => setFromCity(e.target.value)}
//                     className="w-full px-4 py-2 rounded-full border"
//                   />

//                   {viaCities.map((city, index) => (
//                     <div
//                       key={index}
//                       className="w-full px-4 py-2 rounded-full border bg-gray-50 text-sm"
//                     >
//                       📍 {city}
//                     </div>
//                   ))}

//                   <div className="flex gap-2">
//                     <input
//                       type="text"
//                       placeholder="Add city in between"
//                       value={newCity}
//                       onChange={(e) => setNewCity(e.target.value)}
//                       className="flex-1 px-4 py-2 rounded-full border"
//                     />
//                     <button
//                       onClick={addCity}
//                       className="bg-black text-white px-4 rounded-full"
//                     >
//                       + Add
//                     </button>
//                   </div>

//                   <input
//                     type="text"
//                     placeholder="To"
//                     value={toCity}
//                     onChange={(e) => setToCity(e.target.value)}
//                     className="w-full px-4 py-2 rounded-full border"
//                   />

//                   <input
//                     type="time"
//                     value={time}
//                     onChange={(e) => setTime(e.target.value)}
//                     className="w-full px-4 py-2 rounded-full border"
//                   />

//                   <input
//                     type="number"
//                     min={1}
//                     placeholder="Seats"
//                     value={seats}
//                     onChange={(e) => setSeats(Number(e.target.value))}
//                     className="w-full px-4 py-2 rounded-full border"
//                   />
//                 </div>
//               )}
//             </section>

//             {/* RESULTS */}
//             <section className="w-full max-w-md px-4 mt-4 flex-1">
//               <div
//                 className={`rounded-xl p-4 min-h-[200px] ${
//                   search
//                     ? "bg-black text-white"
//                     : "bg-transparent text-gray-400"
//                 }`}
//               >
//                 {mode === "find" &&
//                   filteredRides.map((ride) => (
//                     <div
//                       key={ride.id}
//                       className="flex justify-between items-center bg-white/10 rounded-lg px-4 py-3 mb-2"
//                     >
//                       <div>
//                         <p className="font-semibold">
//                           {ride.route.join(" → ")}
//                         </p>
//                         <p className="text-sm text-gray-300">
//                           {ride.day} • {ride.date} • {ride.time} • Seats: {ride.seats}
//                         </p>
//                       </div>
//                       <button
//                         onClick={() => joinRide(ride)}
//                         className="bg-red-500 text-white px-3 py-1 rounded-full"
//                       >
//                         Join
//                       </button>
//                     </div>
//                   ))}

//                 {mode === "create" && (
//                   <p className="text-center text-gray-500">
//                     Select date, route, and time — then publish when approved
//                   </p>
//                 )}
//               </div>
//             </section>

//             {/* MAP PREVIEW PER RIDE */}
//             {mode === "find" && (
//               <div className="w-full max-w-md px-4 mt-2 space-y-3">
//                 {filteredRides.map((ride) => (
//                   <div key={ride.id} className="rounded-xl overflow-hidden">
//                     {shouldLoadMaps && isLoaded ? (
//                       <GoogleMap
//                         zoom={12}
//                         center={{ lat: 17.385, lng: 78.4867 }}
//                         mapContainerStyle={{
//                           width: "100%",
//                           height: "150px",
//                         }}
//                       >
//                         <Marker position={{ lat: 17.385, lng: 78.4867 }} />
//                       </GoogleMap>
//                     ) : (
//                       <div className="w-full h-[150px] flex items-center justify-center bg-gray-100 text-gray-500 text-sm rounded-xl">
//                         📍 Map preview disabled (Add Google Maps API key)
//                       </div>
//                     )}
//                   </div>
//                 ))}
//               </div>
//             )}

//             {/* PUBLISH BUTTON */}
//             <div className="fixed bottom-4 w-full max-w-md px-4">
//               <button
//                 className="w-full bg-gradient-to-r from-red-300 to-green-300 text-red-600 font-semibold py-4 rounded-full"
//                 onClick={() =>
//                   mode === "create" ? publishRide() : setMode("create")
//                 }
//               >
//                 {mode === "create" ? "Publish Ride →" : "Create Ride →"}
//               </button>
//             </div>
//           </>
//         )}

//         {/* PROFILE PANEL */}
//         {showProfile && (
//           <div className="fixed inset-0 bg-black/40 z-20 flex justify-end">
//             <div className="w-full max-w-md bg-white h-full p-4 space-y-4">
//               <div className="flex justify-between items-center">
//                 <h2 className="text-lg font-bold">My Profile</h2>
//                 <button
//                   className="text-gray-500"
//                   onClick={() => setShowProfile(false)}
//                 >
//                   ✕
//                 </button>
//               </div>

//               <div className="space-y-2">
//                 <label className="text-sm">Name</label>
//                 <input
//                   className="w-full px-4 py-2 rounded-full border"
//                   value={user.name}
//                   onChange={(e) =>
//                     setUser({ ...user, name: e.target.value })
//                   }
//                 />

//                 <label className="text-sm">Mobile Number</label>
//                 <input
//                   className="w-full px-4 py-2 rounded-full border"
//                   placeholder="Enter mobile number"
//                   value={user.phone}
//                   onChange={(e) =>
//                     setUser({ ...user, phone: e.target.value })
//                   }
//                 />

//                 <button
//                   className="w-full bg-black text-white py-2 rounded-full"
//                   onClick={() => {
//                     if (!user.phone) {
//                       toast.error("Enter phone number first");
//                       return;
//                     }
//                     setUser({ ...user, phoneVerified: true });
//                     toast.success("Mobile verified successfully");
//                   }}
//                 >
//                   {user.phoneVerified
//                     ? "Mobile Verified ✔"
//                     : "Verify Mobile"}
//                 </button>
//               </div>

//               <div className="border-t pt-4 space-y-2">
//                 <h3 className="font-semibold">Captain Verification (Optional)</h3>

//                 <p className="text-sm text-gray-500">
//                   Required only to create rides. Verified manually by backend
//                   team.
//                 </p>

//                 <input
//                   className="w-full px-4 py-2 rounded-full border"
//                   placeholder="Driving License Number"
//                 />

//                 <input
//                   className="w-full px-4 py-2 rounded-full border"
//                   placeholder="Vehicle Name"
//                   value={user.vehicle.name}
//                   onChange={(e) =>
//                     setUser({
//                       ...user,
//                       vehicle: {
//                         ...user.vehicle,
//                         name: e.target.value,
//                       },
//                     })
//                   }
//                 />

//                 <input
//                   className="w-full px-4 py-2 rounded-full border"
//                   placeholder="Vehicle Number"
//                   value={user.vehicle.number}
//                   onChange={(e) =>
//                     setUser({
//                       ...user,
//                       vehicle: {
//                         ...user.vehicle,
//                         number: e.target.value,
//                       },
//                     })
//                   }
//                 />

//                 <button
//                   className="w-full bg-blue-500 text-white py-2 rounded-full"
//                   onClick={() =>
//                     toast.success(
//                       "Captain verification request sent to backend"
//                     )
//                   }
//                 >
//                   Submit for Captain Approval
//                 </button>

//                 <p className="text-sm text-gray-500">
//                   Status: {captainStatus}
//                 </p>
//               </div>
//             </div>
//           </div>
//         )}
//       </div>
//     </>
//   );
// }

// // ==============================
// // BASIC TEST CASES (JEST)
// // ==============================
// /*
// import { render, fireEvent } from "@testing-library/react";
// import GoRidesLanding from "./GoRidesLanding";

// test("opens profile panel when profile button is clicked", () => {
//   const { getByText } = render(<GoRidesLanding />);
//   fireEvent.click(getByText("👤"));
//   expect(getByText("My Profile")).toBeInTheDocument();
// });

// test("prevents publishing ride when not approved", () => {
//   const { getByText } = render(<GoRidesLanding />);
//   fireEvent.click(getByText("Captain Mode"));
//   fireEvent.click(getByText("Publish Ride →"));
//   expect(
//     getByText("Captain must be approved before creating rides")
//   ).toBeInTheDocument();
// });
// */




















































// // import React, { useState } from "react";
// // import { ToastContainer, toast } from "react-toastify";
// // import "react-toastify/dist/ReactToastify.css";
// // import { GoogleMap, Marker, Polyline, useJsApiLoader } from "@react-google-maps/api";

// // // ==============================
// // // GO RIDES — LANDING PAGE UI
// // // ==============================

// // // NOTE ABOUT MAP KEY
// // // ------------------
// // // This avoids syntax/runtime errors in sandboxes that don't support import.meta
// // // or process.env. Replace YOUR_GOOGLE_MAPS_KEY with a real key in production.
// // const GOOGLE_MAPS_KEY = ""; // e.g. "AIzaSy..."

// // export default function GoRidesLanding() {
// //   // BASIC APP STATE
// //   const [screen, setScreen] = useState("home"); // home
// //   const [mode, setMode] = useState("find"); // find | create
// //   const [showProfile, setShowProfile] = useState(false);

// //   // USER PROFILE STATE
// //   const [user, setUser] = useState({
// //     name: "Guest User",
// //     phone: "",
// //     phoneVerified: false,
// //     dlVerified: false, // set true manually from backend in real app
// //     vehicle: {
// //       name: "",
// //       number: "",
// //     },
// //   });

// //   // SEARCH / FORM STATE
// //   const [search, setSearch] = useState("");
// //   const [fromCity, setFromCity] = useState("");
// //   const [toCity, setToCity] = useState("");
// //   const [viaCities, setViaCities] = useState([]);
// //   const [newCity, setNewCity] = useState("");
// //   const [time, setTime] = useState("");
// //   const [seats, setSeats] = useState(1);

// //   // CAPTAIN STATUS (FROM BACKEND IN REAL APP)
// //   const captainStatus = user.dlVerified ? "approved" : "pending";

// //   // GOOGLE MAPS LOADER
// //   const { isLoaded } = useJsApiLoader({
// //     googleMapsApiKey: GOOGLE_MAPS_KEY,
// //   });

// //   // DEMO RIDES
// //   const [rides, setRides] = useState([
// //     {
// //       id: 1,
// //       route: ["Madhapur", "Gachibowli"],
// //       time: "9:30 AM",
// //       seats: 1,
// //     },
// //     {
// //       id: 2,
// //       route: ["Ameerpet", "SR Nagar", "Hitech City"],
// //       time: "10:00 AM",
// //       seats: 2,
// //     },
// //   ]);

// //   // FILTER RIDES BY ANY CITY IN ROUTE
// //   const filteredRides = rides.filter((ride) =>
// //     ride.route.some((city) =>
// //       city.toLowerCase().includes(search.toLowerCase())
// //     )
// //   );

// //   const addCity = () => {
// //     if (!newCity.trim()) {
// //       toast.error("Enter a city name before adding");
// //       return;
// //     }
// //     setViaCities([...viaCities, newCity.trim()]);
// //     setNewCity("");
// //     toast.success("City added to route");
// //   };

// //   const publishRide = () => {
// //     if (captainStatus !== "approved") {
// //       toast.error("Captain must be approved before creating rides");
// //       return;
// //     }

// //     if (!fromCity || !toCity) {
// //       toast.error("Please enter From and To cities");
// //       return;
// //     }

// //     const newRide = {
// //       id: Date.now(),
// //       route: [fromCity, ...viaCities, toCity],
// //       time: time || "Anytime",
// //       seats: Number(seats),
// //     };

// //     setRides([newRide, ...rides]);
// //     setFromCity("");
// //     setToCity("");
// //     setViaCities([]);
// //     setTime("");
// //     setSeats(1);

// //     toast.success("Ride Published Successfully 🚀");
// //   };

// //   const joinRide = (ride) => {
// //     if (!user.phoneVerified) {
// //       toast.error("Please verify your mobile number before joining rides");
// //       setShowProfile(true);
// //       return;
// //     }

// //     toast.success(`Join request sent for ${ride.route.join(" → ")}`);
// //   };

// //   return (
// //     <>
// //       <ToastContainer position="top-center" />

// //       <div className="min-h-screen bg-white flex flex-col items-center justify-between relative">
// //         {/* TOP BAR */}
// //         <div className="w-full max-w-md px-4 py-3 flex justify-between items-center fixed top-0 bg-white z-10 border-b">
// //           <button
// //             onClick={() => {
// //               setScreen("home");
// //               setShowProfile(false);
// //             }}
// //             className="font-bold text-lg"
// //           >
// //             GoRides
// //           </button>

// //           <button
// //             onClick={() => setShowProfile(true)}
// //             className="w-9 h-9 rounded-full bg-gray-200 flex items-center justify-center"
// //           >
// //             👤
// //           </button>
// //         </div>

// //         <div className="h-16" />

// //         {/* HOME SCREEN */}
// //         {screen === "home" && (
// //           <>
// //             {/* MODE TOGGLE */}
// //             <div className="w-full max-w-md px-4 mt-4 flex bg-gray-100 rounded-full p-1">
// //               <button
// //                 onClick={() => setMode("find")}
// //                 className={`flex-1 py-2 rounded-full text-sm font-semibold transition ${
// //                   mode === "find" ? "bg-white shadow" : "text-gray-500"
// //                 }`}
// //               >
// //                 Find Ride
// //               </button>
// //               <button
// //                 onClick={() => setMode("create")}
// //                 className={`flex-1 py-2 rounded-full text-sm font-semibold transition ${
// //                   mode === "create" ? "bg-white shadow" : "text-gray-500"
// //                 }`}
// //               >
// //                 Captain Mode
// //               </button>
// //             </div>

// //             {/* SEARCH OR CREATE */}
// //             <section className="w-full max-w-md px-4 mt-4">
// //               {mode === "find" ? (
// //                 <div className="relative">
// //                   <input
// //                     type="text"
// //                     placeholder="Search city on route"
// //                     value={search}
// //                     onChange={(e) => setSearch(e.target.value)}
// //                     className="w-full px-4 py-3 pl-10 rounded-full border"
// //                   />
// //                   <span className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400">
// //                     🔍
// //                   </span>
// //                 </div>
// //               ) : (
// //                 <div className="space-y-2">
// //                   <p className="text-sm text-gray-500">
// //                     Captain status: {captainStatus}
// //                   </p>

// //                   <input
// //                     type="text"
// //                     placeholder="From"
// //                     value={fromCity}
// //                     onChange={(e) => setFromCity(e.target.value)}
// //                     className="w-full px-4 py-2 rounded-full border"
// //                   />

// //                   {viaCities.map((city, index) => (
// //                     <div
// //                       key={index}
// //                       className="w-full px-4 py-2 rounded-full border bg-gray-50 text-sm"
// //                     >
// //                       📍 {city}
// //                     </div>
// //                   ))}

// //                   <div className="flex gap-2">
// //                     <input
// //                       type="text"
// //                       placeholder="Add city in between"
// //                       value={newCity}
// //                       onChange={(e) => setNewCity(e.target.value)}
// //                       className="flex-1 px-4 py-2 rounded-full border"
// //                     />
// //                     <button
// //                       onClick={addCity}
// //                       className="bg-black text-white px-4 rounded-full"
// //                     >
// //                       + Add
// //                     </button>
// //                   </div>

// //                   <input
// //                     type="text"
// //                     placeholder="To"
// //                     value={toCity}
// //                     onChange={(e) => setToCity(e.target.value)}
// //                     className="w-full px-4 py-2 rounded-full border"
// //                   />

// //                   <input
// //                     type="time"
// //                     value={time}
// //                     onChange={(e) => setTime(e.target.value)}
// //                     className="w-full px-4 py-2 rounded-full border"
// //                   />

// //                   <input
// //                     type="number"
// //                     min={1}
// //                     placeholder="Seats"
// //                     value={seats}
// //                     onChange={(e) => setSeats(Number(e.target.value))}
// //                     className="w-full px-4 py-2 rounded-full border"
// //                   />
// //                 </div>
// //               )}
// //             </section>

// //             {/* RESULTS */}
// //             <section className="w-full max-w-md px-4 mt-4 flex-1">
// //               <div
// //                 className={`rounded-xl p-4 min-h-[200px] ${
// //                   search
// //                     ? "bg-black text-white"
// //                     : "bg-transparent text-gray-400"
// //                 }`}
// //               >
// //                 {mode === "find" &&
// //                   filteredRides.map((ride) => (
// //                     <div
// //                       key={ride.id}
// //                       className="flex justify-between items-center bg-white/10 rounded-lg px-4 py-3 mb-2"
// //                     >
// //                       <div>
// //                         <p className="font-semibold">
// //                           {ride.route.join(" → ")}
// //                         </p>
// //                         <p className="text-sm text-gray-300">
// //                           {ride.time} • Seats: {ride.seats}
// //                         </p>
// //                       </div>
// //                       <button
// //                         onClick={() => joinRide(ride)}
// //                         className="bg-red-500 text-white px-3 py-1 rounded-full"
// //                       >
// //                         Join
// //                       </button>
// //                     </div>
// //                   ))}

// //                 {mode === "create" && (
// //                   <p className="text-center text-gray-500">
// //                     Captain must be backend-approved before publishing rides
// //                   </p>
// //                 )}
// //               </div>
// //             </section>

// //             {/* MAP PREVIEW */}
// //             {isLoaded && mode === "create" && fromCity && toCity && (
// //               <div className="w-full max-w-md px-4 mt-2">
// //                 <RideMap
// //                   routePoints={[
// //                     { lat: 17.385, lng: 78.4867 },
// //                     { lat: 17.395, lng: 78.4967 },
// //                   ]}
// //                 />
// //               </div>
// //             )}

// //             {/* PUBLISH BUTTON */}
// //             <div className="fixed bottom-4 w-full max-w-md px-4">
// //               <button
// //                 className="w-full bg-gradient-to-r from-red-300 to-green-300 text-red-600 font-semibold py-4 rounded-full"
// //                 onClick={() =>
// //                   mode === "create"
// //                     ? publishRide()
// //                     : setMode("create")
// //                 }
// //               >
// //                 {mode === "create"
// //                   ? "Publish Ride →"
// //                   : "Create Ride →"}
// //               </button>
// //             </div>
// //           </>
// //         )}

// //         {/* PROFILE SLIDE-IN PANEL */}
// //         {showProfile && (
// //           <div className="fixed inset-0 bg-black/40 z-20 flex justify-end">
// //             <div className="w-full max-w-md bg-white h-full p-4 space-y-4">
// //               <div className="flex justify-between items-center">
// //                 <h2 className="text-lg font-bold">My Profile</h2>
// //                 <button
// //                   className="text-gray-500"
// //                   onClick={() => setShowProfile(false)}
// //                 >
// //                   ✕
// //                 </button>
// //               </div>

// //               <div className="space-y-2">
// //                 <label className="text-sm">Name</label>
// //                 <input
// //                   className="w-full px-4 py-2 rounded-full border"
// //                   value={user.name}
// //                   onChange={(e) =>
// //                     setUser({ ...user, name: e.target.value })
// //                   }
// //                 />

// //                 <label className="text-sm">Mobile Number</label>
// //                 <input
// //                   className="w-full px-4 py-2 rounded-full border"
// //                   placeholder="Enter mobile number"
// //                   value={user.phone}
// //                   onChange={(e) =>
// //                     setUser({ ...user, phone: e.target.value })
// //                   }
// //                 />

// //                 <button
// //                   className="w-full bg-black text-white py-2 rounded-full"
// //                   onClick={() => {
// //                     if (!user.phone) {
// //                       toast.error("Enter phone number first");
// //                       return;
// //                     }
// //                     setUser({ ...user, phoneVerified: true });
// //                     toast.success("Mobile verified successfully");
// //                   }}
// //                 >
// //                   {user.phoneVerified
// //                     ? "Mobile Verified ✔"
// //                     : "Verify Mobile"}
// //                 </button>
// //               </div>

// //               <div className="border-t pt-4 space-y-2">
// //                 <h3 className="font-semibold">
// //                   Captain Verification (Optional)
// //                 </h3>

// //                 <p className="text-sm text-gray-500">
// //                   Required only to create rides. Verified manually by backend
// //                   team.
// //                 </p>

// //                 <input
// //                   className="w-full px-4 py-2 rounded-full border"
// //                   placeholder="Driving License Number"
// //                 />

// //                 <input
// //                   className="w-full px-4 py-2 rounded-full border"
// //                   placeholder="Vehicle Name"
// //                   value={user.vehicle.name}
// //                   onChange={(e) =>
// //                     setUser({
// //                       ...user,
// //                       vehicle: {
// //                         ...user.vehicle,
// //                         name: e.target.value,
// //                       },
// //                     })
// //                   }
// //                 />

// //                 <input
// //                   className="w-full px-4 py-2 rounded-full border"
// //                   placeholder="Vehicle Number"
// //                   value={user.vehicle.number}
// //                   onChange={(e) =>
// //                     setUser({
// //                       ...user,
// //                       vehicle: {
// //                         ...user.vehicle,
// //                         number: e.target.value,
// //                       },
// //                     })
// //                   }
// //                 />

// //                 <button
// //                   className="w-full bg-blue-500 text-white py-2 rounded-full"
// //                   onClick={() =>
// //                     toast.success(
// //                       "Captain verification request sent to backend"
// //                     )
// //                   }
// //                 >
// //                   Submit for Captain Approval
// //                 </button>

// //                 <p className="text-sm text-gray-500">
// //                   Status: {captainStatus}
// //                 </p>
// //               </div>
// //             </div>
// //           </div>
// //         )}
// //       </div>
// //     </>
// //   );
// // }

// // // ==============================
// // // SMART FARE SPLITTING ALGORITHM (DISTANCE BASED)
// // // ==============================

// // export function calculateFare(
// //   totalDistanceKm,
// //   totalFuelCost,
// //   riderDistances
// // ) {
// //   if (!totalDistanceKm || totalDistanceKm <= 0) {
// //     throw new Error("Total distance must be greater than 0");
// //   }

// //   const costPerKm = totalFuelCost / totalDistanceKm;

// //   return riderDistances.map((d) => ({
// //     distance: d,
// //     fare: Math.round(d * costPerKm),
// //   }));
// // }

// // // ==============================
// // // MAP COMPONENT
// // // ==============================

// // function RideMap({ routePoints }) {
// //   if (!routePoints || !routePoints.length) return null;

// //   return (
// //     <GoogleMap
// //       zoom={12}
// //       center={routePoints[0]}
// //       mapContainerStyle={{
// //         width: "100%",
// //         height: "200px",
// //         borderRadius: "16px",
// //       }}
// //     >
// //       {routePoints.map((p, i) => (
// //         <Marker key={i} position={p} />
// //       ))}
// //       <Polyline
// //         path={routePoints}
// //         options={{ strokeColor: "#ef4444", strokeWeight: 4 }}
// //       />
// //     </GoogleMap>
// //   );
// // }

// // // ==============================
// // // BASIC TEST CASES (DEV / JEST)
// // // ==============================

// // /*
// // import { calculateFare } from "./GoRidesLanding";

// // test("splits fare correctly by distance", () => {
// //   const result = calculateFare(20, 200, [5, 10, 5]);
// //   expect(result).toEqual([
// //     { distance: 5, fare: 50 },
// //     { distance: 10, fare: 100 },
// //     { distance: 5, fare: 50 },
// //   ]);
// // });

// // test("throws error when distance is zero", () => {
// //   expect(() => calculateFare(0, 100, [5])).toThrow();
// // });
// // */

// // // ==============================
// // // NOTE
// // // ==============================
// // // - GoRides header returns home
// // // - Profile opens as slide-in panel with close button
// // // - Mobile verification required to join rides
// // // - Captain verification required to create rides
// // // - Captain approval is backend/manual





// import React, { useState } from "react";
// import { GoogleMap, Marker, Polyline, useJsApiLoader } from "@react-google-maps/api";

// // HomeScreen Component
// const HomeScreen = () => {
//   // ---------- STATE ----------
//   const [screen, setScreen] = useState("home"); // currently only home screen
//   const [mode, setMode] = useState("find"); // find or create
//   const [search, setSearch] = useState("");
//   const [fromCity, setFromCity] = useState("");
//   const [toCity, setToCity] = useState("");
//   const [viaCities, setViaCities] = useState([]);
//   const [newCity, setNewCity] = useState("");
//   const [time, setTime] = useState("");
//   const [seats, setSeats] = useState(1);
//   const [captainStatus, setCaptainStatus] = useState("Pending");

//   const [rides, setRides] = useState([
//     {
//       id: 1,
//       route: [
//         { lat: 19.076, lng: 72.8777 },
//         { lat: 19.2, lng: 72.9 },
//       ],
//       nameRoute: ["Mumbai", "Thane"],
//       time: "10:30",
//       seats: 3,
//     },
//     {
//       id: 2,
//       route: [
//         { lat: 19.076, lng: 72.8777 },
//         { lat: 19.1, lng: 72.95 },
//       ],
//       nameRoute: ["Mumbai", "Navi Mumbai"],
//       time: "12:00",
//       seats: 2,
//     },
//   ]);

//   // ---------- FILTERED RIDES ----------
//   const filteredRides = rides.filter((ride) =>
//     ride.nameRoute.join(" ").toLowerCase().includes(search.toLowerCase())
//   );

//   // ---------- GOOGLE MAPS LOADER ----------
//   const { isLoaded } = useJsApiLoader({
//     googleMapsApiKey: import.meta.env.VITE_GOOGLE_MAPS_KEY,
//   });

//   // ---------- FUNCTIONS ----------
//   const addCity = () => {
//     if (newCity.trim() !== "") {
//       setViaCities([...viaCities, newCity.trim()]);
//       setNewCity("");
//     }
//   };

//   const publishRide = () => {
//     if (!fromCity || !toCity || !time || !seats) {
//       alert("Please fill all required fields!");
//       return;
//     }

//     const newRide = {
//       id: rides.length + 1,
//       route: [
//         { lat: 19.076, lng: 72.8777 },
//         { lat: 19.2, lng: 72.9 },
//       ], // Replace with real geocoding for each city
//       nameRoute: [fromCity, ...viaCities, toCity],
//       time: time,
//       seats: seats,
//     };
//     setRides([...rides, newRide]);
//     alert("Ride Published Successfully!");

//     // Reset fields
//     setFromCity("");
//     setToCity("");
//     setViaCities([]);
//     setNewCity("");
//     setTime("");
//     setSeats(1);
//   };

//   const joinRide = (ride) => {
//     alert(`Joined ride: ${ride.nameRoute.join(" → ")}`);
//   };

//   // ---------- JSX ----------
//   return (
//     <div className="min-h-screen flex flex-col items-center bg-gray-50 py-6">
//       {screen === "home" && (
//         <>
//           {/* MODE TOGGLE */}
//           <div className="w-full max-w-md px-4 flex bg-gray-100 rounded-full p-1 mb-4">
//             <button
//               onClick={() => setMode("find")}
//               className={`flex-1 py-2 rounded-full text-sm font-semibold transition ${
//                 mode === "find" ? "bg-white shadow" : "text-gray-500"
//               }`}
//             >
//               Find Ride
//             </button>
//             <button
//               onClick={() => setMode("create")}
//               className={`flex-1 py-2 rounded-full text-sm font-semibold transition ${
//                 mode === "create" ? "bg-white shadow" : "text-gray-500"
//               }`}
//             >
//               Captain Mode
//             </button>
//           </div>

//           {/* SEARCH OR CREATE */}
//           <section className="w-full max-w-md px-4 mb-4">
//             {mode === "find" ? (
//               <div className="relative">
//                 <input
//                   type="text"
//                   placeholder="Search city on route"
//                   value={search}
//                   onChange={(e) => setSearch(e.target.value)}
//                   className="w-full px-4 py-3 pl-10 rounded-full border"
//                 />
//                 <span className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400">
//                   🔍
//                 </span>
//               </div>
//             ) : (
//               <div className="space-y-2">
//                 <p className="text-sm text-gray-500">Captain status: {captainStatus}</p>
//                 <input
//                   type="text"
//                   placeholder="From"
//                   value={fromCity}
//                   onChange={(e) => setFromCity(e.target.value)}
//                   className="w-full px-4 py-2 rounded-full border"
//                 />

//                 {viaCities.map((city, index) => (
//                   <div
//                     key={index}
//                     className="w-full px-4 py-2 rounded-full border bg-gray-50 text-sm"
//                   >
//                     📍 {city}
//                   </div>
//                 ))}

//                 <div className="flex gap-2">
//                   <input
//                     type="text"
//                     placeholder="Add city in between"
//                     value={newCity}
//                     onChange={(e) => setNewCity(e.target.value)}
//                     className="flex-1 px-4 py-2 rounded-full border"
//                   />
//                   <button onClick={addCity} className="bg-black text-white px-4 rounded-full">
//                     + Add
//                   </button>
//                 </div>

//                 <input
//                   type="text"
//                   placeholder="To"
//                   value={toCity}
//                   onChange={(e) => setToCity(e.target.value)}
//                   className="w-full px-4 py-2 rounded-full border"
//                 />

//                 <input
//                   type="time"
//                   value={time}
//                   onChange={(e) => setTime(e.target.value)}
//                   className="w-full px-4 py-2 rounded-full border"
//                 />
//                 <input
//                   type="number"
//                   min={1}
//                   placeholder="Seats"
//                   value={seats}
//                   onChange={(e) => setSeats(e.target.value)}
//                   className="w-full px-4 py-2 rounded-full border"
//                 />
//               </div>
//             )}
//           </section>

//           {/* RESULTS */}
//           <section className="w-full max-w-md px-4 flex-1 mb-16">
//             <div
//               className={`rounded-xl p-4 min-h-[200px] ${
//                 search ? "bg-black text-white" : "bg-transparent text-gray-400"
//               }`}
//             >
//               {mode === "find" &&
//                 filteredRides.map((ride) => (
//                   <div
//                     key={ride.id}
//                     className="flex flex-col justify-between items-start bg-white/10 rounded-lg px-4 py-3 mb-4"
//                   >
//                     <p className="font-semibold">{ride.nameRoute.join(" → ")}</p>
//                     <p className="text-sm text-gray-300">
//                       {ride.time} • Seats: {ride.seats}
//                     </p>
//                     {isLoaded && (
//                       <GoogleMap
//                         zoom={10}
//                         center={ride.route[0]}
//                         mapContainerStyle={{ width: "100%", height: "200px", borderRadius: "16px", marginTop: "8px" }}
//                       >
//                         <Polyline
//                           path={ride.route}
//                           options={{ strokeColor: "#ef4444", strokeWeight: 4 }}
//                         />
//                         {ride.route.map((p, i) => (
//                           <Marker key={i} position={p} />
//                         ))}
//                       </GoogleMap>
//                     )}
//                     <button
//                       onClick={() => joinRide(ride)}
//                       className="bg-red-500 text-white px-3 py-1 rounded-full mt-2"
//                     >
//                       Join
//                     </button>
//                   </div>
//                 ))}

//               {mode === "create" && (
//                 <p className="text-center text-gray-500">
//                   Captain must be admin-approved before publishing rides
//                 </p>
//               )}
//             </div>
//           </section>

//           {/* PUBLISH BUTTON */}
//           {mode === "create" && (
//             <div className="fixed bottom-4 w-full max-w-md px-4">
//               <button
//                 className="w-full bg-gradient-to-r from-red-300 to-green-300 text-red-600 font-semibold py-4 rounded-full"
//                 onClick={publishRide}
//               >
//                 Publish Ride →
//               </button>
//             </div>
//           )}
//         </>
//       )}
//     </div>
//   );
// };

// export default HomeScreen;

