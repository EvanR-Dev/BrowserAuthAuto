import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword } from "firebase/auth";

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
            const user = userCredential.user;
            return null;
        })
        .catch((error) => {
            return error.message as string;
        });
};