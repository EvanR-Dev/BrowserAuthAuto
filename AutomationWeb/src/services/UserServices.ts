import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword, sendPasswordResetEmail} from "firebase/auth";
import { store } from "@/stores/index"
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
            
            store.password = password;
            store.username = email;
            return null;
        })
        .catch((error) => {
            return error.message as string;
        });
};

export const logOutUser = (): Promise<string | null> => {
    const auth = getAuth();
    return auth.signOut()
        .then(() => {
            document.cookie = "CurrentUser" + "=" + null;
            store.password = '';
            store.username = '';
            return null;
        })
        .catch((error) => {
            return error.message as string;
        })
}

// make sure email exists, then send email
export const recoverUser = (email: string): Promise<string | null> => {
    const auth = getAuth();
    return sendPasswordResetEmail(auth, email)
        .then(() => {
            // Password reset email sent!
            return null;
        })
        .catch((error) => {
            return error.message as string;
        });
};