function checkAuth() {
  const token = localStorage.getItem("token");
  const authArea = document.getElementById("authArea");

  if(token){
    authArea.innerHTML = `<button onclick="logout()">Logout</button>`;
  } else {
    authArea.innerHTML = `<button onclick="openAuth()">Login</button>`;
  }
}

function openAuth(){
  document.getElementById("authModal").classList.remove("hidden");
}

function logout(){
  localStorage.removeItem("token");
  location.reload();
}

async function login(){
  try{
    showLoader();
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const res = await apiRequest("/auth/login","POST",{email,password});
    localStorage.setItem("token",res.access_token);

    hideLoader();
    showToast("Login successful");
    location.reload();
  }catch(err){
    hideLoader();
    showToast(err.message);
  }
}

async function register(){
  try{
    showLoader();
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    await apiRequest("/auth/register","POST",{email,password});
    hideLoader();
    showToast("Registered successfully");
  }catch(err){
    hideLoader();
    showToast(err.message);
  }
}

checkAuth();