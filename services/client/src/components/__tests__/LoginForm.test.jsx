import React from "react";
import { render, cleanup } from "@testing-library/react";

import LoginForm from "../LoginForm";

afterEach(cleanup);

it("renders properly", () => {
  const { getByText } = render(<LoginForm />);
  expect(getByText("Log In")).toHaveClass("title");
});

it("renders", () => {
  const { asFragment } = renderWithRouter(<LoginForm />);
  expect(asFragment()).toMatchSnapshot();
});
