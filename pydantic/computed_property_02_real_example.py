from pydantic import BaseModel, Field, computed_field


class Invoice(BaseModel):
    subtotal: float = Field(gt=0)
    tax_percent: float = Field(ge=0, le=100)

    @computed_field
    @property
    def tax_amount(self) -> float:
        return round(
            self.subtotal * self.tax_percent / 100,
            2
        )

    @computed_field
    @property
    def grand_total(self) -> float:
        return round(
            self.subtotal + self.tax_amount,
            2
        )


invoice = Invoice(
    subtotal=100,
    tax_percent=18
)
print(invoice.tax_amount)
print(invoice.grand_total)
print(invoice.model_dump())