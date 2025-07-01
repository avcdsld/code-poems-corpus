def current_portfolio_weights(self):
        """
        Compute each asset's weight in the portfolio by calculating its held
        value divided by the total value of all positions.

        Each equity's value is its price times the number of shares held. Each
        futures contract's value is its unit price times number of shares held
        times the multiplier.
        """
        position_values = pd.Series({
            asset: (
                    position.last_sale_price *
                    position.amount *
                    asset.price_multiplier
            )
            for asset, position in self.positions.items()
        })
        return position_values / self.portfolio_value