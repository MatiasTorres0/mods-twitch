// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDioEonJwXlaNohJ7zrQcmuq1RnhfT51XY",
  authDomain: "mods-cdc1f.firebaseapp.com",
  projectId: "mods-cdc1f",
  storageBucket: "mods-cdc1f.firebasestorage.app",
  messagingSenderId: "748214015699",
  appId: "1:748214015699:web:d2339874c6d017636ea626",
  measurementId: "G-GYFGVLQNSH"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);