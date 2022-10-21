import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword, sendPasswordResetEmail} from "firebase/auth";

export const createUser = (email: string, password: string): Promise<string | null> => {
    const auth = getAuth();
    return createUserWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            // Signed in 
            const user = userCredential.user;
            return null;
        })
        .catch((error) => {
            return error.message as string;
        });
};

export const logInUser = (email: string, password: string): Promise<string | null> => {
    const auth = getAuth();
    return signInWithEmailAndPassword(auth, email, password)
        .then((userCredential) => {
            // Signed in 

            document.cookie = "CurrentUser" + "=" + JSON.stringify(userCredential.user);

            console.log(decodeURIComponent(document.cookie))
            const user = userCredential.user;

            return null;
        })
        .catch((error) => {
            return error.message as string;
        });
};

// make sure email exists, then send email
export const recoverUser = (email: string): Promise<string | null> => {
    const auth = getAuth();
    return sendPasswordResetEmail(auth, email)
        .then(() => {
            // Password reset email sent!
            // ..
            return "Success";
        })
        .catch((error) => {
            const errorCode = error.code;
            const errorMessage = error.message;
            return error.message as string;
            // ..
        });
};